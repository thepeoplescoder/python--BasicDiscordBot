# Imports
import inspect
import functools

# enforce_type ############################################
def enforce_type(obj, _type):
    """Raises an exception if the given object does not match the given type,
    otherwise returns the object."""
    if isinstance(obj, _type):
        return obj
    raise TypeError(''.join(
        [
            "Value {0} must be of type {1}.  ".format(obj, type),
            "Please check your code.",
        ]
    ))

# package_path ############################################
def package_path(dunder_file):
    from pathlib import Path
    return Path(dunder_file).resolve().parent

# get_modules_from ########################################
def get_modules_from(path):
    from pkgutil import iter_modules
    return iter_modules([str(path)])        # Force string to avoid PosixPath/startswith bug

# to_coroutine ############################################
def to_coroutine(obj, *args, **kwargs):
    """Intent of this function:

    Normal functions passed are now usable in await expressions.
    Awaitables silently pass through.  Arguments are evaluated,
    but ignored.
    """
    return obj if inspect.isawaitable(obj) else async_wrap(obj)(*args, **kwargs)

# async_wrap ##############################################
def async_wrap(f):
    """Wraps normal function into an async def"""
    if inspect.iscoroutinefunction(f):
        return f
    elif inspect.isawaitable(f):
        raise ValueError(f"Unexpected awaitable of type {type(f)} passed: {f}")
    elif not callable(f):
        raise ValueError(f"Expected callable, got {type(f)}")

    @functools.wraps(f)
    async def wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wrapper

# is_command_match ########################################
async def is_command_match(ctx, name, *, print=async_wrap(print)):
    if not ctx.command:
        await print("No command received by this listener.")
        return False

    elif ctx.command.name != name:
        await print(f"Command \"{ctx.command.name}\" does not match \"{name}\"")
        return False

    return True
