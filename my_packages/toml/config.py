# Third party imports
import toml as _toml

# Load the configuration file.
try:
    toml = ".config.toml"
    toml = _toml.load(toml)
except FileNotFoundError as ex:
    import sys
    from ..common import terminal as t
    print(t.yellow(f"{toml} not found.  Either create the file yourself"))
    print(t.yellow("or check this directory to see if any .toml files can"))
    print(t.yellow("be renamed as such."))
    print()
    print(t.yellow("Did you forget to copy config.toml to .config.toml?"))
    sys.exit(1)

# Convenience symbols for top-level items.
discord    = toml['discord']
database   = toml['database']
developer  = toml['developer']
servers    = toml['servers']

# Merge select lists of strings into single strings.
discord['token'] = ''.join(discord['token'])

# is_developer_id #########################################
def is_developer_id(user_id):
    return user_id in developer['ids']

# If we're running this as a script,
# then show the configuration.
if __name__ == "__main__":
    from pprint import pprint
    pprint(toml)