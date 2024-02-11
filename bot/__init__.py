import logging

from .my_packages.bot    import Bot
from .my_packages.common import terminal as t
from .my_packages.toml   import config

# main ####################################################
async def main():
    """Entry point.  Allow asynchronous context immediately."""
    color = t.bright_yellow

    # Are we supposed to be directing the user's attention to .config.toml?
    if config.toml["app"]["direct_attention_to_dot_config_dot_toml_and_exit"]:
        print(color("Please examine .config.toml to make sure"))
        print(color("that it is configured to your requirements."))

    # Otherwise, run the bot as normal.
    else:
        print("Starting bot application.")

        # Set up logging
        print(color("Setting up logging..."))
        logging.basicConfig(level=logging.INFO)

        # Set up the bot.
        print(t.bright_blue("Loading bot.  This may take a few moments."))
        bot = await Bot.async_create_instance()                             # ;-)
        print(t.bright_blue("Bot loaded successfully."))

        # Okay, it's ready to run!
        await bot.run_async()
