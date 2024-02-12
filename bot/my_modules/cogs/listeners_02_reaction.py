# 3rd party imports
from discord import Reaction
from discord import Member
from discord import User
from discord import Message
from discord import RawReactionActionEvent
from discord import RawReactionClearEvent
from discord import RawReactionClearEmojiEvent

# Local imports
from . import BaseCog
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_reaction_add #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_add(self, reaction: Reaction, user: Member | User) -> None:
        pass

    # on_raw_reaction_add #################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent) -> None:
        pass

    # on_reaction_remove ##################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_remove(self, reaction: Reaction, user: Member | User) -> None:
        pass

    # on_raw_reaction_remove ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_reaction_remove(self, payload: RawReactionActionEvent) -> None:
        pass

    # on_reaction_clear ###################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_clear(self, message: Message, reactions: list[Reaction]) -> None:
        pass

    # on_raw_reaction_clear ###############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_raw_reaction_clear(self, payload: RawReactionClearEvent) -> None:
        pass

    # on_reaction_clear_emoji #############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_reaction_clear_emoji(self, payload: RawReactionClearEmojiEvent) -> None:
        pass
