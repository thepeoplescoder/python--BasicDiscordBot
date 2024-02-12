# 3rd party imports
from discord import Message

# Local imports
from . import BaseCog
from ..common import decorators
from ..common import terminal as t
from ..types import ClassVar

# class Cog ###############################################
class Cog(BaseCog, name=BaseCog.create_cog_name(__name__)):
    ADD_TO_BOT: ClassVar[bool] = True

    # on_message ##########################################
    @BaseCog.listener()
    @decorators.async_with_header(__name__)
    async def on_message(self, message: Message) -> None:
        """This function simply logs all messages to
        the console that the bot is aware of."""

        # Display the message object received.
        await self.bot.print(t.bright_black(str(message)))

        # Display when the message was sent.
        await self.bot.print(end=t.bright_green('['))
        await self.bot.print(end=t.green(str(message.created_at)))
        await self.bot.print(end=t.bright_green("] "))

        # Display the channel that the message is coming from.
        await self.bot.print(end=t.bright_green('['))
        if hasattr(message.channel, "guild"):
            await self.bot.print(end=t.yellow(str(message.channel.guild)))
            await self.bot.print(end=t.bright_yellow(" #"))
        await self.bot.print(end=t.bright_yellow(str(message.channel)))
        await self.bot.print(end=t.bright_green(']'))
        await self.bot.print()

        # Display who the message is coming from
        await self.bot.print(end=t.bright_blue(message.author.name))
        await self.bot.print(end=t.blue('#'))
        await self.bot.print(end=t.bright_blue(message.author.discriminator))
        await self.bot.print(end=t.bright_yellow(": "))

        # And lastly, display the message.
        await self.bot.print(t.bright_cyan(message.content))

        # (TBD) If there is an attachment, handle it.
        pass