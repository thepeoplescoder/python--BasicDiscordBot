# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_member_ban #######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_ban(self, guild, user):
        pass

    # on_member_unban #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_unban(self, guild, user):
        pass
