# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_invite_create ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_invite_create(self, invite):
        pass

    # on_invite_delete ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_invite_delete(self, invite):
        pass