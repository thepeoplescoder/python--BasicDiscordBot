import datetime

# 3rd party imports
from discord import User
from discord import Member
from discord import Message
from discord import RawMessageDeleteEvent
from discord import RawMessageUpdateEvent
from discord import RawBulkMessageDeleteEvent
from discord.abc import Messageable

# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_typing ###########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_typing(self, channel: Messageable, user: User | Member, when: datetime.datetime) -> None:
        pass

    # on_message ##########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message(self, message: Message) -> None:
        pass

    # on_message_delete ###################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message_delete(self, message: Message) -> None:
        pass

    # on_bulk_message_delete ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_bulk_message_delete(self, messages: list[Message]) -> None:
        pass

    # on_raw_message_delete ###############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_message_delete(self, payload: RawMessageDeleteEvent) -> None:
        pass

    # on_raw_bulk_message_delete ##########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_bulk_message_delete(self, payload: RawBulkMessageDeleteEvent) -> None:
        pass

    # on_message_edit #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message_edit(self, before: Message, after: Message) -> None:
        pass

    # on_raw_message_edit #################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_message_edit(self, payload: RawMessageUpdateEvent) -> None:
        pass
