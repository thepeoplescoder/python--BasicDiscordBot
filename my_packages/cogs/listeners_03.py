# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_webhooks_update ##################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_webhooks_update(self, channel):
        pass

    # on_voice_state_update ###############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_voice_state_update(self, member, before, after):
        pass
