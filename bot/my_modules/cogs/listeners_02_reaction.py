# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_reaction_add #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_add(self, reaction, user):
        pass

    # on_raw_reaction_add #################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_reaction_add(self, payload):
        pass

    # on_reaction_remove ##################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_remove(self, reaction, user):
        pass

    # on_raw_reaction_remove ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_reaction_remove(self, payload):
        pass

    # on_reaction_clear ###################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_clear(self, message, reactions):
        pass

    # on_raw_reaction_clear ###############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_reaction_clear(self, payload):
        pass

    # on_reaction_clear_emoji #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_clear_emoji(self, payload):
        pass
