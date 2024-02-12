import datetime

# Local imports
from discord import Thread
from discord import GroupChannel
from discord.abc import PrivateChannel
from discord.abc import GuildChannel

from . import BaseCog
from ..common import decorators
from ..types import Optional

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # See https://discordpy.readthedocs.io/en/v2.3.2/migrating.html?highlight=on_private_channel_delete
    #
    # on_private_channel_delete ###########################
    # @BaseCog.listener()
    # @decorators.async_with_header(__name__)
    # async def on_private_channel_delete(self, channel: PrivateChannel):
    #     pass

    # See https://discordpy.readthedocs.io/en/v2.3.2/migrating.html?highlight=on_private_channel_create
    #
    # on_private_channel_create ###########################
    # @BaseCog.listener()
    # @decorators.async_with_header(__name__)
    # async def on_private_channel_create(self, channel: PrivateChannel):
    #     pass

    # on_private_channel_update ###########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_private_channel_update(self, before: GroupChannel, after: GroupChannel):
        pass

    # on_private_channel_pins_update ######################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_private_channel_pins_update(self, channel: PrivateChannel, last_pin: Optional[datetime.datetime]):
        pass

    # on_guild_channel_delete #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_delete(self, channel: GuildChannel):
        pass

    # on_guild_channel_create #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_create(self, channel: GuildChannel):
        pass

    # on_guild_channel_update #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_update(self, before: GuildChannel, after: GuildChannel):
        pass

    # on_guild_channel_pins_update ########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_pins_update(self, channel: GuildChannel | Thread, last_pin: Optional[datetime.datetime]):
        pass
