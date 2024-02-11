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
        x = util.is_command_match
        x = x(ctx, self.developer.name, print=self.bot.print)
        if not await x:
            return

        # Access denied!
        await cheeky_responses.say("who_are_you", ctx)

        # Show the context object.
        await self.bot.print("-----Context Object-----")
        v = vars(ctx)
        for key in v:
            await self.bot.print(t.bright_green(f"{key}: ") + str(v[key]))

    # logout ##############################################
    @developer.command(aliases=["logoff", "shutdown", "exit"])
    async def logout(self, ctx):
        """Causes the bot to log out of Discord."""
        await ctx.send("Going offline...")
        await self.bot.logout()

    # push_clients ########################################
    @developer.command()
    async def push_clients(self, ctx):
        num_clients = len(self.bot.server_managers["push"])
        use_plural = int(num_clients != 1)
        plurals = {
            "is":     {True: "are",     False: "is"},
            "client": {True: "clients", False: "client"},
        }
        await ctx.send(
            "There {} currently **{}** {} connected to the push server.".format(
                plurals["is"][use_plural],
                num_clients,
                plurals["client"][use_plural],
            )
        )