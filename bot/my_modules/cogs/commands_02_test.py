# Imports
from pprint import pprint

# 3rd party imports
import discord.ext.commands
from discord.ext.commands import CommandError
from discord.ext.commands import Context

# Local imports
from . import BaseCog
from ..common import util
from ..common import decorators
from ..common import terminal as t

from ..toml import config

from ..types import ClassVar

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    """Test commands"""
    ADD_TO_BOT: ClassVar[bool] = True

    # developer ###########################################
    @discord.ext.commands.group()
    @discord.ext.commands.check(lambda ctx: config.is_developer_id(ctx.author.id))
    async def test(self, ctx: Context) -> None:
        """Testing grounds."""
        await self.bot.print("Inside test()")
        await ctx.send("test() function called...")

    # logout ##############################################
    @test.command()
    async def logout(self, ctx):
        await ctx.send("Going offline...")
        await self.bot.logout()

    # on_command_error ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_command_error(self, ctx: Context, exception: CommandError) -> None:
        if not await util.is_command_match(ctx, "test", async_print=self.bot.print):
            return

        # Show the context object.
        await self.bot.print("-----Context Object-----")
        await self.bot.pprint(ctx)
        ctx_dict = vars(ctx)
        await util.async_show_dict({key: ctx_dict[key]
                                    for key in ctx_dict if key != "message"}, async_print=self.bot.print)

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