# 3rd party imports
from discord.ext.commands import Context
from discord.ext.commands import CommandError

# Imports
from . import BaseCog
from ..common import util
from ..common import terminal as t
from ..common import decorators
from ..types import ClassVar

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT: ClassVar[bool] = True

    # on_command_error ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_command_error(self, ctx: Context, exception: CommandError) -> None:
        """Something bad happened?  This is where we go."""
        exception_type:    str = t.black_on_bright_red ( f"{type(exception)}:" )
        exception_message: str = t.bright_red          ( str(exception)        )

        await self.bot.print(f"{exception_type} {exception_message}\n")
        await util.async_show_context_object(ctx, async_print=self.bot.print)