# Third party imports
import toml as _toml
from ..types import Any
from ..types import TypedDict

_CONFIG_FILE_NAME = ".config.toml"

class DotConfigDotTomlDict(TypedDict):
    """Describes the format of .config.toml."""
    class DiscordDict(TypedDict):
        token: str
    class DatabaseDict(TypedDict):
        host: str
        port: int
        username: str
        password: str
    class DeveloperDict(TypedDict):
        ids: list[int]
        debug: bool
        guilds: dict[str, int]
    class ServersDict(TypedDict):
        class ServerTypeDict(TypedDict):
            port: int
            file: str
        http: ServerTypeDict
        push: ServerTypeDict

    discord:   DiscordDict
    database:  DatabaseDict
    developer: DeveloperDict
    servers:   ServersDict

# Load the configuration file.
try:
    toml: DotConfigDotTomlDict = _toml.load(_CONFIG_FILE_NAME)
except FileNotFoundError as ex:
    import sys
    from ..common import terminal as t
    print(t.yellow(f"{_CONFIG_FILE_NAME} not found.  Either create the file yourself"))
    print(t.yellow("or check this directory to see if any .toml files can"))
    print(t.yellow("be renamed as such."))
    print()
    print(t.yellow("Did you forget to copy config.toml to .config.toml?"))
    sys.exit(1)

# Convenience symbols for top-level items.
discord   = toml['discord']
database  = toml['database']
developer = toml['developer']
servers   = toml['servers']

# Merge select lists of strings into single strings.
discord['token'] = ''.join(discord['token'])

# is_developer_id #########################################
def is_developer_id(user_id: int) -> bool:
    """Does this ID belong to the developer? `true` if it does, otherwise `false`."""
    return user_id in developer['ids']

# If we're running this as a script,
# then show the configuration.
if __name__ == "__main__":
    from pprint import pprint
    pprint(toml)