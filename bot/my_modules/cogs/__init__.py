##############################################
#                                            #
#   Initialization module for package cogs   #
#                                            #
##############################################

#
# This directory will contain all of the cogs needed by the bot.
#

# Imports
# import sys
from types import ModuleType

# Third party imports
# import discord
import discord.ext.commands as _api_commands

# Local imports
from ..common import terminal as t
from ..common.util import package_path, get_modules_from
from ..types import enforce_type
from ..types import ClassVar

# Useful aliases
CogType = _api_commands.Cog

# class BaseCog ###########################################
class BaseCog(CogType):
    """Base class for all cogs in this application."""
    internals: ClassVar[ModuleType] = _api_commands

    # This is set to true if add_all_cogs() should automatically add
    # this cog to the bot.  By default, this is set to False, meaning
    # cogs should explicitly set this value to be added.
    ADD_TO_BOT: bool = False

    # __init__ ############################################
    def __init__(self, bot: _api_commands.Bot, *args, **kwargs) -> None:
        """Constructor.  Ensures that the attached object is a bot."""
        super().__init__(*args, **kwargs)
        self.bot = enforce_type(bot, _api_commands.Bot)

    # get_cog_name ########################################
    @classmethod
    def get_cog_name(cls) -> str:
        return cls.__cog_name__

    # create_cog_name #####################################
    @staticmethod
    def create_cog_name(dunder_name: str) -> str:
        return dunder_name + ".Cog"

# add_all_cogs ############################################
async def add_all_cogs(bot: _api_commands.Bot) -> None:
    """Adds all cogs in this package to the specified bot."""
    from importlib import import_module

    # Look at every module in this subpackage.
    for module_info in get_modules_from(package_path(__file__)):
        module: ModuleType    = import_module(f".{module_info.name}", __package__)
        attach_this_cog: bool = hasattr(module, "Cog") and issubclass(module.Cog, BaseCog) and module.Cog.ADD_TO_BOT

        if attach_this_cog:
            await bot.add_cog(module.Cog(bot))
            color = t.bright_green
        else:
            color = t.bright_black

        print(color(module.__name__))