import discord.ext.commands
from discord.ext.commands import Cog
from discord.ext.commands import Command

from ..types import Any
from ..types import Mapping
from ..types import Callable

class HelpCommand(discord.ext.commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()

    async def send_bot_help(self, mapping: Mapping[Cog | None, list[Command[Any, Callable[..., Any], Any]]]) -> None:
        await self.get_destination().send(f"Calling {self.send_bot_help.__name__}...")
        await super().send_bot_help(mapping)
        s = ["```"]
        for cog in mapping:
            category: str = "No Category" if cog is None else cog.__doc__
            command_names: list[str] = [command.name for command in mapping[cog]]
            if command_names:
                s.append(f"{category}: {command_names}")
        s.append("```")
        s = '\n'.join(s)
        await self.get_destination().send(s)

    async def send_cog_help(self, cog: Cog) -> None:
        await self.get_destination().send(f"Calling {self.send_cog_help.__name__}...")
        return await super().send_cog_help(cog)

    async def send_command_help(self, command: Command[Any, Callable[..., Any], Any]) -> None:
        await self.get_destination().send(f"Calling {self.send_command_help.__name__}...")
        return await super().send_command_help(command)

    async def send_group_help(self, group: discord.ext.commands.Group[Any, Callable[..., Any], Any]) -> None:
        await self.get_destination().send(f"Calling {self.send_group_help.__name__}...")
        return await super().send_group_help(group)