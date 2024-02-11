# Local imports
from . import BaseCog

from ..toml import config
from ..toml import cheeky_responses

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT = True

    # logout ##############################################
    @BaseCog.internals.command()
    async def logout(self, ctx):
        if config.is_developer_id(ctx.author.id):
            await ctx.send("Goodbye everyone!")
            await ctx.send("Logging out...")
            await self.bot.logout()
        else:
            await cheeky_responses.say("who_are_you", ctx)
            await cheeky_responses.say("shutdown_denied", ctx)

    # hello ###############################################
    @BaseCog.internals.command()
    async def hello(self, ctx):
        await ctx.send("this is the hello command.")

    # multiply ############################################
    @BaseCog.internals.command()
    async def multiply(self, ctx, x: float, y: float):
        await ctx.send("**{0}** x **{1}** = **{2}**".format(x, y, x * y))