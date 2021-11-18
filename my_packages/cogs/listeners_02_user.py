# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_user_update ######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_user_update(self, before, after):
        pass
