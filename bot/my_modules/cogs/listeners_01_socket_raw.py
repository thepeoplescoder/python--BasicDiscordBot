# Imports
import json
from pprint import pprint

# Local imports
from . import BaseCog
from ..common import decorators
from ..common import terminal as t

from ..types import ClassVar

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT: ClassVar[bool] = False

    # __init__ ############################################
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__zlib = None

    # on_socket_raw_receive ###############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_socket_raw_receive(self, msg):

        # If we have binary data, decompress it.
        if isinstance(msg, bytes):
            if len(msg) < 4 or msg[-4:] != b"\x00\x00\xFF\xFF":
                return
            await self.bot.print(t.black_on_bright_red("Decompressed data (zlib):"))
            msg = self.bot.zlib_decompress(msg).decode("utf-8")

        # Pretty print the JSON object.
        await self.bot.print(end=t.bright_red)
        await self.bot.pprint(json.loads(msg))
        await self.bot.print(end=t.normal)

    # on_socket_raw_send ##################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_socket_raw_send(self, payload: bytes | str):
        if isinstance(payload, bytes):
            payload = payload.decode("utf-8")
        await self.bot.print(t.bright_green(payload))
