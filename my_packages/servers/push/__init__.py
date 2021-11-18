######################################################
#                                                    #
#   Initialization module for servers.push package   #
#                                                    #
######################################################

# Imports
# import socket
import asyncio
import contextlib
import os

# Local imports
from .. import BaseServerManager
from ...common import terminal as t

# class ServerManager #####################################
class ServerManager(BaseServerManager):

    # __init__ ############################################
    def __init__(self, **kwargs):
        super().__init__()

        x = kwargs["address_file"]
        assert isinstance(x, str) and x

        self.__write_buffer      = dict()
        self.__write_buffer_lock = asyncio.Lock()
        self.__address_file_name = x

    # close ###############################################
    async def close(self):
        await super().close()                   # This call is required.
        os.remove(self.__address_file_name)     # Intentionally blocking

    # start_server ########################################
    async def start_server(self, host, port):
        """A wrapper around asyncio.start_server(), specific
        to this application."""

        # Create a server socket and start the server if
        # a server isn't already started.
        if not self.server:
            from socket import socket
            sock = socket()
            sock.bind((host, port))
            sock.listen()

            # Write the address information to the address file.
            # I don't care about this being blocking; as a matter
            # of fact, it is intentional.
            with open(self.__address_file_name, "w") as fp:
                print("{0}\n{1}".format(*sock.getsockname()), file=fp)

            # This actually starts the server and sets the server property.
            await super().start_server(sock=sock)

        # Return the server object.
        return self.server

    # get_write_buffer_for ################################
    def get_write_buffer_for(self, *connection):
        """Gets the write buffer for a specific connection
        and returns it immediately."""
        return self.__write_buffer.setdefault(connection[:2], [])

    # lock_all_write_buffers_to_use_only ##################
    @contextlib.asynccontextmanager
    async def lock_all_write_buffers_to_use_only(self, *connection):
        """Locks every write buffer so only one for a specific connection
        can be used."""
        await self.__write_buffer_lock.acquire()
        try:
            yield self.get_write_buffer_for(*connection)
        finally:
            self.__write_buffer_lock.release()

    # write_buffer_append #################################
    async def write_buffer_append(self, data):
        """Queues up data to be sent to every connected client."""
        async with self.__write_buffer_lock:
            for connection in self.connections:
                self.get_write_buffer_for(*connection).append(data)

    # close_connection ####################################
    async def close_connection(self, reader, writer):
        """Silently closes a connection."""
        await super().close_connection(reader, writer)

        # Remove the write buffer associated with the connection.
        async with self.__write_buffer_lock:
            if (reader, writer) in self.__write_buffer:
                del self.__write_buffer[(reader, writer)]

    # on_client_connect ###################################
    async def on_client_connect(self, *connection):
        await super().on_client_connect(*connection)    # Required.

        # Display connect status
        writer = connection[1]
        address = writer.get_extra_info("peername")
        await self.print(t.bright_yellow(f"Connected to client {address}"))
        await self.print(t.bright_yellow(f"can_write_eof: {writer.can_write_eof()}\n"))

        # Remove the last two lines printed from the
        # current client's write buffer.  They should
        # know that they're connecting, so we don't
        # need to state the obvious here.
        buf = self.get_write_buffer_for(*connection)
        del buf[0]
        del buf[0]

        # Here, we're just sending messages that we queue
        # to all of our connected clients.
        try:
            from time import time
            checktime = time()
            checks_per_second = 4               # Four per second is plenty.
            interval = 1.0 / checks_per_second

            while True:
                try:
                    # This is basically a sanity check to ensure
                    # that the client is still available.
                    if time() >= checktime:
                        checktime = time() + interval
                        writer.write(" \b".encode("utf-8"))
                        await writer.drain()

                    # This used to not be needed.  Now it's needed or
                    # the bot essentially freezes.  Why?
                    await asyncio.sleep(0)

                    # Get the write buffer for this connection and get the next
                    # available message in the queue.
                    async with self.lock_all_write_buffers_to_use_only(*connection) as buf:
                        try:
                            data = buf[0]
                            del buf[0]
                        except IndexError:
                            data = None

                    # If we have data to write, then send it to the client.
                    if data:
                        writer.write(data)

                        # Runtime error happens here,
                        # I'm just being slightly verbose.
                        try:
                            await writer.drain()
                        except RuntimeError:
                            raise

                # Leave the loop if we have disconnected.
                except (ConnectionError, RuntimeError):
                    break

        # Just in case anything unexpected shows up...
        except Exception as ex:
            await self.print(t.bright_blue(f"Why are we here? {ex}"))
            raise

        # Disconnect, do cleanup, and show a status message
        finally:
            await self.close_connection(*connection)
            await self.print(
                t.bright_red(f"Disconnected from client {address}\n")
            )
