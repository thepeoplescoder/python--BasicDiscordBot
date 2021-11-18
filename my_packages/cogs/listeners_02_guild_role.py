# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_guild_role_create ################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_role_create(self, role):
        pass

    # on_guild_role_delete ################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_role_delete(self, role):
        pass

    # on_guild_role_update ################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_role_update(self, before, after):
        pass
