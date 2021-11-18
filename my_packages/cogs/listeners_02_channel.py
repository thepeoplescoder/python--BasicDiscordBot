# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_private_channel_delete ###########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_private_channel_delete(self, channel):
        pass

    # on_private_channel_create ###########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_private_channel_create(self, channel):
        pass

    # on_private_channel_update ###########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_private_channel_update(self, before, after):
        pass

    # on_private_channel_pins_update ######################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_private_channel_pins_update(self, channel, last_pin):
        pass

    # on_guild_channel_delete #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_delete(self, channel):
        pass

    # on_guild_channel_create #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_create(self, channel):
        pass

    # on_guild_channel_update #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_update(self, before, after):
        pass

    # on_guild_channel_pins_update ########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_channel_pins_update(self, channel, last_pin):
        pass
