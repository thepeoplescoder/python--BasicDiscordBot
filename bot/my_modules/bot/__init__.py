#############################################
#                                           #
#   Initialization module for package bot   #
#                                           #
#############################################

# Imports
import asyncio
import zlib
import builtins
from io import StringIO

# Third party imports
import discord.ext.commands

# Local imports
from ..common  import terminal as t
from ..common  import decorators
from ..toml    import config
from ..servers import BaseServerManager
from ..servers import push
from ..types import Self
from ..types import Buffer
from ..types import TypedDict
from ..types import ClassVar

from .helpcommand import HelpCommand

# class _ServerManagerDict ################################
class _ServerManagerDict(TypedDict):
    """Describes a server manager dictionary."""
    push: push.ServerManager
    http: BaseServerManager

# class Bot ###############################################
class Bot(discord.ext.commands.Bot):
    _instance: ClassVar[Self] = None

    server_managers: _ServerManagerDict
    __zlib = zlib.decompressobj()

    # async_get_instance ##################################
    @classmethod
    async def async_get_instance(cls) -> Self:
        """Gets the singleton instance of this class.  If it
        does not exist yet, then an instance of this class is
        created, attaching objects that must be initialized in
        an async context."""
        async def main() -> Self:
            return cls._instance if cls._instance else await create_and_initialize_instance()

        async def create_and_initialize_instance() -> Self:
            b = cls()
            await add_all_cogs_to(b)
            b.server_managers["push"] = await setup_and_start_push_server(b)
            return b

        async def add_all_cogs_to(bot: Self) -> None:
            from .. import cogs
            await cogs.add_all_cogs(bot)

        async def setup_and_start_push_server(bot: Self) -> push.ServerManager:
            settings = config.toml["servers"]["push"]
            psm = push.ServerManager(address_file=settings["file"])
            await psm.start_server('', settings["port"])
            psm.print = bot.print
            return psm

        return await main()

    # __init__ ############################################
    def __init__(self) -> None:
        """Constructor.  It is preferred to get the singleton instance
        of this class in an asynchronous context via the
        Bot.async_get_instance() function."""
        self.__ensure_singleton_naive()

        super().__init__(
            intents=discord.Intents.all(),
            command_prefix=discord.ext.commands.when_mentioned,
            help_command=HelpCommand(),
        )

        self.server_managers = dict()

        # Use our custom print function for the header
        # decorators so the output can be echoed to all
        # clients directly connected to our socket.
        decorators.async_with_header.set_print(self.print)

    # __ensure_singleton_naive ############################
    def __ensure_singleton_naive(self):
        """Ensures only one instance of this class exists.  Not thread safe."""
        if __class__._instance:
            raise TypeError(f"Only one instance of {__class__} can exist.")
        __class__._instance = self

    # run_async ###########################################
    async def run_async(self) -> None:
        """Entry point for the bot."""
        color = t.bright_yellow
        sm_push: push.ServerManager = self.server_managers["push"]

        print(color("Running bot..."))

        token: str = config.toml["discord"]["token"]

        async with sm_push.server:
            try:
                await asyncio.gather(self.start(token), sm_push.server.start_serving())
            finally:
                await self.close()
                await sm_push.close()
                print(color("Bot terminated!"))

    # print ###############################################
    async def print(self, *args, **kwargs) -> None:
        s = StringIO()
        builtins.print(*args, **kwargs, file=s)

        await self.__finish_printing(s.getvalue())

    # pprint ##############################################
    async def pprint(self, *args, **kwargs) -> None:
        """Pretty printer that uses our enhanced print."""
        from pprint import pprint as _pprint

        s = StringIO()
        _pprint(*args, **kwargs, stream=s)

        await self.__finish_printing(s.getvalue())

    # __finish_printing ###################################
    async def __finish_printing(self, s: str) -> None:
        """Prints the text s to the console and forwards it to every
        client connected to the push server."""
        builtins.print(end=s)
        await self.server_managers["push"].write_buffer_append(s.encode("utf-8"))

    # zlib_decompress #####################################
    def zlib_decompress(self, msg: Buffer) -> bytes:
        """Uses the zlib module to decompress `msg`."""
        while True:
            try:
                return self.__zlib.decompress(msg)

            # Create a new decompression object either if one
            # does not exist, or if the existing one fails.
            except (AttributeError, zlib.error):
                self.__zlib = zlib.decompressobj()
