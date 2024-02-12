# Local imports
from discord import Guild
from discord import Member
from discord import User

from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_member_ban #######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_ban(self, guild: Guild, user: Member | User):
        pass

    # on_member_unban #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_unban(self, guild: Guild, user: User):
        pass
