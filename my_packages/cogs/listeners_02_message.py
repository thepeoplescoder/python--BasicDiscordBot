# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_typing ###########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_typing(self, channel, user, when):
        pass

    # on_message ##########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message(self, message):
        pass

    # on_message_delete ###################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message_delete(self, message):
        pass

    # on_bulk_message_delete ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_bulk_message_delete(self, messages):
        pass

    # on_raw_message_delete ###############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_message_delete(self, payload):
        pass

    # on_raw_bulk_message_delete ##########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_bulk_message_delete(self, payload):
        pass

    # on_message_edit #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message_edit(self, before, after):
        pass

    # on_raw_message_edit #################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_message_edit(self, payload):
        pass
