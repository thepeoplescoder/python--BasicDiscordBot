# Third party imports
from pathlib import Path
import toml as _toml

# Load the configuration file.
try:
    toml = Path(__file__).parent / "tomls" / "cheeky_responses.toml"
    toml = str(toml)
    toml = _toml.load(toml)

# In this case, it's a fatal error if we can't find the .toml file.
except FileNotFoundError as ex:
    import sys
    from ..common import terminal as t
    print(end=t.bright_red("Fatal error: "))
    print(t.bright_yellow(f"{toml} not found."))
    print()
    toml = toml.name
    print(t.bright_yellow(f"Did you forget to copy _{toml} to {toml}?"))
    print(t.bright_yellow("Symbolic links work, too."))
    sys.exit(1)

# say #####################################################
async def say(key, to_context):
    """Echoes the requested string in the table to the given text channel
    (provided as a context object)."""
    src = toml[key]
    if isinstance(src, str):        # Convert strings to one-element lists.
        src = [src]
    for item in src:
        await to_context.send(item)