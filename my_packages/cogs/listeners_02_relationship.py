# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_relationship_add #################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_relationship_add(self, relationship):
        pass

    # on_relationship_remove ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_relationship_remove(self, relationship):
        pass

    # on_relationship_update ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_relationship_update(self, before, after):
        pass
