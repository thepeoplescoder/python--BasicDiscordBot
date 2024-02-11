# Imports
from . import BaseCog
from ..common import terminal as t
from ..common import util
from ..common import decorators

from ..toml import config
from ..toml import cheeky_responses

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT = True

    # developer ###########################################
    @BaseCog.internals.group(aliases=["sudo", "superuser"])
    @BaseCog.internals.check(lambda ctx: config.is_developer_id(ctx.author.id))
    async def developer(self, ctx):
        """Developer-exclusive commands."""
        await ctx.send(":clown: `Executing developer command...` :clown:")

    # on_command_error ####################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_command_error(self, ctx, exception):
        """This function handles the error scenario for "developer"
        commands."""

        # Leave if the command category doesn't match.
        if not await util.is_command_match(ctx, self.developer.name, async_print=self.bot.print):
            return

        await cheeky_responses.say("who_are_you", ctx)
        await util.async_show_context_object(ctx, async_print=self.bot.print)

    # logout ##############################################
    @developer.command(aliases=["logoff", "shutdown", "exit"])
    async def logout(self, ctx):
        """Causes the bot to log out of Discord."""
        await ctx.send("Going offline...")
        await self.bot.close()

    # push_clients ########################################
    @developer.command()
    async def push_clients(self, ctx):
        num_clients = len(self.bot.server_managers["push"])
        w = util.plural_dict(num_clients, are="is", clients="client")
        await ctx.send(f"There {w['are']} currently **{num_clients}** {w['clients']} connected to the push server.")