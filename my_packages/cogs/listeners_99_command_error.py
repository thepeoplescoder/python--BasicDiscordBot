# Imports
from . import BaseCog
from ..common import terminal as t
from ..common import decorators

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT = True

    # on_command_error ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_command_error(self, ctx, exception):
        """Something bad happened?  This is where we go."""
        await self.bot.print(t.black_on_bright_red("Reason:"), end=' ')
        await self.bot.print(t.bright_red(str(exception)))

        # Show the context object.
        await self.bot.print("-----Context Object-----")
        v = vars(ctx)
        for key in v:
            await self.bot.print(t.bright_green(f"{key}: ") + str(v[key]))
