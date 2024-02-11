# Imports
from pprint import pprint

# Local imports
from . import BaseCog
from ..common import util
from ..common import decorators
from ..common import terminal as t

from ..toml import config

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT = True

    # developer ###########################################
    @BaseCog.internals.group()
    @BaseCog.internals.check(lambda ctx: not config.is_developer_id(ctx.author.id))
    async def test(self, ctx):
        """Testing grounds."""
        await self.bot.print("Inside test()")
        await ctx.send("test() function called...")

    # on_command_error ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_command_error(self, ctx, exception):
        x = util.is_command_match
        x = x(ctx, "test", print=self.bot.print)
        if not await x:
            return

        # Show the context object.
        await self.bot.print("-----Context Object-----")
        await self.bot.pprint(ctx)
        v = vars(ctx)
        for key in v:
            if key == "message":
                continue
            await self.bot.print(t.bright_green(f"{key}: ") + str(v[key]))

        # Show the message object of the context object last.
        #
        # This is how you iterate through the attributes of
        # an object if __slots__ is defined.
        for attr in ctx.message.__slots__:
            if hasattr(ctx.message, attr):
                await self.bot.print(end=t.bright_blue(f"{attr}: "))            # name
                val = getattr(ctx.message, attr)
                await self.bot.print(t.bright_yellow(str(type(val))), end=' ')  # type
                await self.bot.print(t.bright_red(str(val)))                    # value

    # logout ##############################################
    @test.command()
    async def logout(self, ctx):
        await ctx.send("Going offline...")
        await self.bot.logout()