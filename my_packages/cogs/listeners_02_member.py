# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_member_join ######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_join(self, member):
        pass

    # on_member_remove ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_remove(self, member):
        pass

    # on_member_update ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_member_update(self, before, after):
        pass
