# 3rd party imports
from discord import Guild
from discord import Emoji

# Local imports
from . import BaseCog
from ..common import decorators
from ..types import Sequence

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):

    # on_guild_available ##################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_available(self, guild: Guild) -> None:
        pass

    # on_guild_unavailable ################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_unavailable(self, guild: Guild) -> None:
        pass

    # on_guild_join #######################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_join(self, guild: Guild) -> None:
        pass

    # on_guild_remove #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_remove(self, guild: Guild) -> None:
        pass

    # on_guild_update #####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_update(self, before: Guild, after: Guild) -> None:
        pass

    # on_guild_emojis_update ##############################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_emojis_update(self, guild: Guild, before: Sequence[Emoji], after: Sequence[Emoji]) -> None:
        pass

    # on_guild_integrations_update ########################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_guild_integrations_update(self, guild: Guild) -> None:
        pass
