# Imports
import discord.ext.commands
from discord.ext.commands import Context
from discord.ext.commands import CommandError

from . import BaseCog
from ..common import terminal as t
from ..common import util
from ..common import decorators

from ..toml import config
from ..toml import cheeky_responses

from ..types import ClassVar

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    """Developer Commands"""
    ADD_TO_BOT: ClassVar[bool] = True

    # developer ###########################################
    @discord.ext.commands.group(aliases=["sudo", "superuser"])
    @discord.ext.commands.check(lambda ctx: config.is_developer_id(ctx.author.id))
    async def developer(self, ctx: Context) -> None:
        """Developer-exclusive commands."""
        await ctx.send(":clown: `Executing developer command...` :clown:")

    # logout ##############################################
    @developer.command(aliases=["logoff", "shutdown", "exit"])
    async def logout(self, ctx: Context) -> None:
        """Causes the bot to log out of Discord."""
        await ctx.send("Going offline...")
        await self.bot.close()

    # push_clients ########################################
    @developer.command()
    async def push_clients(self, ctx: Context) -> None:
        num_clients: int  = len(self.bot.server_managers["push"])
        w: dict[str, str] = util.plural_dict(num_clients, are="is", clients="client")
        await ctx.send(f"There {w['are']} currently **{num_clients}** {w['clients']} connected to the push server.")

    # on_command_error ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_command_error(self, ctx: Context, exception: CommandError) -> None:
        """This function handles the error scenario for "developer"
        commands."""
        if not await self.is_this_command_a_group_match(context=ctx, group=self.developer):
            return
        await cheeky_responses.say("who_are_you", ctx)
        await util.async_show_context_object(ctx, async_print=self.bot.print)