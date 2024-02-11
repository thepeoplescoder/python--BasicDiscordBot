# Imports
import inspect
import functools

from . import terminal as t

# enforce_type ############################################
def enforce_type(obj, _type):
    """Raises an exception if the given object does not match the given type,
    otherwise returns the object."""
    if isinstance(obj, _type):
        return obj
    raise TypeError(f"Value {obj} must be of type {_type}.  Please check your code.")

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
async def is_command_match(ctx, name, *, async_print=async_wrap(print)):
    if not ctx.command:
        await async_print("No command received by this listener.")
        return False

    elif ctx.command.name != name:
        await async_print(f"Command \"{ctx.command.name}\" does not match \"{name}\"")
        return False

    return True

async def async_show_dict(d, *, header=None, async_print=async_wrap(print)):
    if isinstance(header, str):
        await async_print(header)
    for key in d:
        await async_print( t.bright_green(f"{key}: ") + str(d[key]) )

# show_context_object #####################################
async def async_show_context_object(ctx, *, async_print=async_wrap(print)):
    await async_show_dict(vars(ctx), header="-----Context Object-----", async_print=async_print)

# plural_dict #############################################
def plural_dict(n, **kwargs_plural_to_singular) -> dict:
    is_plural = float(n) != 1
    result = {}
    for plural_form in kwargs_plural_to_singular:
        result[plural_form] = plural_form if is_plural else kwargs_plural_to_singular[plural_form]
    return result