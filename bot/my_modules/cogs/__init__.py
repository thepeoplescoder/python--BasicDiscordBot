##############################################
#                                            #
#   Initialization module for package cogs   #
#                                            #
##############################################

#
# This directory will contain all of the cogs needed by the bot.
#

# Imports
from types import ModuleType
from importlib import import_module
from pkgutil import ModuleInfo


# Third party imports
import discord.ext.commands as _api_commands
from discord.ext.commands import Context
from discord.ext.commands import Group

# Local imports
from ..common import terminal as t
from ..common.util import package_path, get_modules_from
from ..common.util import is_command_match
from ..types import enforce_type
from ..types import ClassVar
from ..types import Iterator
from ..bot import Bot

# Useful aliases
CogType = _api_commands.Cog

# class BaseCog ###########################################
class BaseCog(CogType):
    """Base class for all cogs in this application."""

    # This is set to true if add_all_cogs() should automatically add
    # this cog to the bot.  By default, this is set to False, meaning
    # cogs should explicitly set this value to be added.
    ADD_TO_BOT: ClassVar[bool] = False

    bot: Bot

    # __init__ ############################################
    def __init__(self, bot: Bot, *args, **kwargs) -> None:
        """Constructor.  Ensures that the attached object is a bot."""
        super().__init__(*args, **kwargs)
        self.bot = enforce_type(bot, Bot)

    # get_cog_name ########################################
    @classmethod
    def get_cog_name(cls) -> str:
        return cls.__cog_name__

    # create_cog_name #####################################
    @staticmethod
    def create_cog_name(dunder_name: str) -> str:
        return dunder_name + ".Cog"
    
    # is_this_command_a_group_match #######################
    async def is_this_command_a_group_match(self, *, context: Context, group: Group) -> bool:
        return await is_command_match(context, group.name, async_print=self.bot.print)

# add_all_cogs ############################################
async def add_all_cogs(bot: _api_commands.Bot) -> None:
    """Adds all cogs in this package to the specified bot."""
    every_module_in_this_subpackage: Iterator[ModuleInfo] = get_modules_from(package_path(__file__))

    for module_info in every_module_in_this_subpackage:
        module: ModuleType  = import_module(f".{module_info.name}", __package__)
        is_cog_module: bool = hasattr(module, "Cog") and issubclass(module.Cog, BaseCog)

        if is_cog_module:
            if module.Cog.ADD_TO_BOT:
                await bot.add_cog(module.Cog(bot))
                color = t.bright_green
            else:
                color = t.bright_black
            print(color(module.__name__))