# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    """These events were for user bots, but they are no longer supported.
    
    Source: https://github.com/Rapptz/discord.py/discussions/9732"""

    # on_group_join #######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_group_join(self, channel, user):
        pass

    # on_group_remove #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_group_remove(self, channel, user):
        pass
