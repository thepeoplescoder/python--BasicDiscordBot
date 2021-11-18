# Local imports
from . import BaseCog
from ..common import decorators
from ..common import terminal as t

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT = True

    # on_ready ############################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_ready(self):

        # Show login info
        await self.bot.print(f"{t.bright_blue(str(self.bot.user))} has connected to Discord!")
        await self.bot.print()
        await self.bot.print("Logged in as:")
        await self.bot.print(self.bot.user.name)
        await self.bot.print(self.bot.user.id)
        await self.bot.print("-------------")
        await self.bot.print()
        #return

        # Show info about connected guilds
        for guild in self.bot.guilds:
            await self.bot.print(f"{t.bright_yellow_on_blue(str(guild))} -> {guild.id}")
            for member in guild.members:
                await self.bot.print(f"\t{member} -> {member.id}")
