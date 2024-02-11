# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_connect ##########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_connect(self):
        pass

    # on_disconnect #######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_disconnect(self):
        pass

    # on_resume ###########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_resumed(self):
        pass
