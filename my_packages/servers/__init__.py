#################################################
#                                               #
#   Initialization module for servers package   #
#                                               #
#################################################

# Imports
import asyncio

# Local imports
from ..common import util
from ..common import terminal as t

# class BaseServerManager #################################
class BaseServerManager(object):

    # __init__ ############################################
    def __init__(self):
        self.__connections = dict()     # (StreamReader, StreamWriter) -> socket.socket
                                        # Keeps track of OPEN connections.
        self.__server      = None
        self.__printer     = util.async_wrap(print)

    # __len__ #############################################
    def __len__(self):
        """The number of active connections."""
        return len(self.__connections)

    # property print ######################################
    @property
    def print(self):
        return self.__printer

    # property print ######################################
    @print.setter
    def print(self, f):
        self.__printer = f

    # property connections ################################
    @property
    def connections(self):
        """The clients connected to the server.  A copy of the
        internal list is returned."""
        return self.__connections.copy()

    # property server #####################################
    @property
    def server(self):
        """The asyncio.Server object being managed."""
        return self.__server

    # close_connection ####################################
    async def close_connection(self, reader, writer):
        """Silently close a connection."""
        if (reader, writer) in self.__connections:

            # Send an EOF to the peer if possible.
            if writer.can_write_eof():
                try:
                    writer.write_eof()
                    await writer.drain()
                except ConnectionError:
                    pass

            # Apparently this code can throw an exception.
            try:
                writer.close()
                await writer.wait_closed()
            except ConnectionError:
                pass

            # We don't need this anymore.
            del self.__connections[(reader, writer)]

    # close ###############################################
    async def close(self):
        """Stops the server (TBD) and closes all client connections."""
        for key in self.connections:
            await self.close_connection(*key)

    # on_client_connect ###################################
    async def on_client_connect(self, reader, writer):
        """This gets called whenever a client connects. Subclasses
        overriding this function are still required to call it."""

        # Keep track of the new connection.
        if (reader, writer) not in self.__connections:
            self.__connections[(reader, writer)] = writer.get_extra_info('socket')

    # start_server ########################################
    async def start_server(self, sock):
        """A wrapper around asyncio.start_server(), specific to this application."""
        if not self.__server:
            self.__server = await asyncio.start_server(
                self.on_client_connect, sock=sock,
            )
        return self.__server