# Local imports
from . import BaseCog

import discord.ext.commands
from discord.ext.commands import Context

from ..toml import config
from ..toml import cheeky_responses
from ..types import ClassVar

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    """Basic Commands"""
    ADD_TO_BOT: ClassVar[bool] = True

    # logout ##############################################
    @discord.ext.commands.command()
    async def logout(self, ctx: Context) -> None:
        """Logs the bot out of Discord.  Only works for the developer."""
        if config.is_developer_id(ctx.author.id):
            await ctx.send("Goodbye everyone!")
            await ctx.send("Logging out...")
            await self.bot.close()
        else:
            await cheeky_responses.say("who_are_you",     ctx)
            await cheeky_responses.say("shutdown_denied", ctx)

    # hello ###############################################
    @discord.ext.commands.command()
    async def hello(self, ctx: Context) -> None:
        """A basic command that says hello."""
        await ctx.send("Hello!")

    # multiply ############################################
    @discord.ext.commands.command(aliases=["product", "mul"])
    async def multiply(self, ctx: Context, x: float, y: float) -> None:
        """Multiplies two numbers."""
        await ctx.send(f"**{x}** x **{y}** = **{x * y}**")
