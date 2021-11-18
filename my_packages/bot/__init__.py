#############################################
#                                           #
#   Initialization module for package bot   #
#                                           #
#############################################

# Imports
import asyncio
import zlib

# Third party imports
import discord.ext.commands

# Local imports
from ..common  import terminal as t
from ..common  import decorators
from ..toml    import config
from ..servers import push

# class Bot ###############################################
class Bot(discord.ext.commands.Bot):

    # create_instance #####################################
    @classmethod
    async def async_create_instance(cls, *args, **kwargs):
        """Creates an instance of this class and attaches
        objects that must be initialized in an async context
        to it."""
        obj = cls(*args, **kwargs)

        # Dictionary of server managers.
        obj.server_managers = dict()

        # Push server manager.
        settings = config.toml["servers"]["push"]
        x = push.ServerManager(address_file=settings["file"])
        await x.start_server('', settings["port"])
        x.print = obj.print

        # Add it to the server manager dictionary.
        obj.server_managers["push"] = x

        # Return the newly created object.
        return obj

    # __init__ ############################################
    def __init__(self, *args, **kwargs):
        """Constructor.  It is preferred to create an instance
        of this class in an asynchronous context via the
        Bot.async_create_instance() function."""
        super().__init__(
            intents=discord.Intents.all(),
            command_prefix=discord.ext.commands.when_mentioned,
        )

        # Attach all cogs to the bot.
        # This is where the "magic" happens, as all the code
        # allowing the bot to listen to events happens in these
        # two lines of code.
        from .. import cogs
        cogs.add_all_cogs(self)

        # This is for zlib_decompress().
        self.__zlib = None

        # Use our custom print function for the header
        # decorators so the output can be echoed to all
        # clients directly connected to our socket.
        decorators.async_with_header.set_print(self.print)

    # run_async ###########################################
    async def run_async(self):
        """Entry point for the bot."""
        color   = t.bright_yellow
        sm_push = self.server_managers["push"]

        print(color("Running bot..."))

        async with sm_push.server:
            try:
                await asyncio.gather(
                    self.start(config.toml["discord"]["token"]),
                    sm_push.server.start_serving(),
                )
            finally:
                await self.close()
                await sm_push.close()
                print(color("Bot terminated!"))

    # print ###############################################
    async def print(self, *args, **kwargs):
        from builtins import print as _print
        from io import StringIO

        # Create the string to print.
        s = StringIO()
        _print(*args, **kwargs, file=s)
        s = s.getvalue()

        await self.__finish_printing(s)

    # __finish_printing ###################################
    async def __finish_printing(self, s):
        """Prints the text s to the console and forwards it to every
        client connected to the push server."""
        from builtins import print as _print
        _print(end=s)
        await self.server_managers["push"].write_buffer_append(s.encode("utf-8"))

    # pprint ##############################################
    async def pprint(self, *args, **kwargs):
        """Pretty printer that uses our enhanced print."""
        from pprint import pprint as _pprint
        from io import StringIO
        s = StringIO()
        _pprint(*args, **kwargs, stream=s)
        s = s.getvalue()

        await self.__finish_printing(s)

    # zlib_decompress #####################################
    def zlib_decompress(self, msg):
        while True:
            try:
                return self.__zlib.decompress(msg)

            # Create a new decompression object either if one
            # does not exist, or if the existing one fails.
            except (AttributeError, zlib.error):
                self.__zlib = zlib.decompressobj()
