# Imports
import inspect
import functools
import numbers

from pathlib import Path
from pkgutil import iter_modules
from pkgutil import ModuleInfo

from discord.ext.commands import Context

from . import terminal as t
from ..types import Callable
from ..types import Iterator
from ..types import Any
from ..types import Coroutine
from ..types import StrPath
from ..types import PrintCoroutineFunction

# package_path ############################################
def package_path(dunder_file: StrPath) -> Path:
    return Path(dunder_file).resolve().parent

# get_modules_from ########################################
def get_modules_from(path: object) -> Iterator[ModuleInfo]:
    return iter_modules([str(path)])        # Force string to avoid PosixPath/startswith bug

# to_coroutine ############################################
# def to_coroutine(obj, *args, **kwargs):
#     """Intent of this function:

#     Normal functions passed are now usable in await expressions.
#     Awaitables silently pass through.  Arguments are evaluated,
#     but ignored.
#     """
#     return obj if inspect.isawaitable(obj) else async_wrap(obj)(*args, **kwargs)

# async_wrap ##############################################
def async_wrap[**T, U](
        f: Callable[T, U] | Callable[T, Coroutine[Any, Any, U]]
    ) -> Callable[T, Coroutine[Any, Any, U]]:
    """Wraps normal function into an async def"""
    if inspect.iscoroutinefunction(f):
        return f
    elif inspect.isawaitable(f):
        raise TypeError(f"Unexpected awaitable of type {type(f)} passed: {f}")
    elif not callable(f):
        raise TypeError(f"Expected callable, got {type(f)}")

    @functools.wraps(f)
    async def wrapper(*args, **kwargs) -> U:
        return f(*args, **kwargs)
    return wrapper

# is_command_match ########################################
async def is_command_match(ctx: Context, name: str, *, async_print: PrintCoroutineFunction=async_wrap(print)) -> bool:
    if ctx.command.name == name:
        return True

    if ctx.command:
        await async_print(f"Command \"{ctx.command.name}\" does not match \"{name}\"")
    else:
        await async_print("No command received by this listener.")

    return False

# async_show_dict #########################################
async def async_show_dict(d: dict, *, header: str=None, async_print: PrintCoroutineFunction=async_wrap(print)):
    if isinstance(header, str):
        await async_print(header)
    for key in d:
        await async_print( t.bright_green(f"{key}: ") + str(d[key]) )

# show_context_object #####################################
async def async_show_context_object(ctx: Context, *, async_print: PrintCoroutineFunction=async_wrap(print)):
    await async_show_dict(vars(ctx), header="-----Context Object-----", async_print=async_print)

# plural_dict #############################################
def plural_dict(n: numbers.Real, **kwargs_plural_to_singular: str) -> dict[str, str]:
    is_plural = float(n) != 1
    result = {}
    for plural_form in kwargs_plural_to_singular:
        result[plural_form] = plural_form if is_plural else kwargs_plural_to_singular[plural_form]
    return result