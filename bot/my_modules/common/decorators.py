from ..types import PrintCoroutineFunction
from ..types import Callable
from ..types import Awaitable

# async_with_header #######################################
def async_with_header():
    import functools
    from . import util
    from . import terminal as t

    _print = util.async_wrap(print)

    def set_print(func: PrintCoroutineFunction=_print) -> None:
        nonlocal _print
        _print = func

    # The actual closure that will end up being used.
    def async_with_header(dunder_name: str):
        """Decorates an `async` function that prints header information
        to the console when called.  Used mainly for listeners.
        
        `dunder_name` is literally the `__name__` symbol in the file where
        the function is being declared.
        """
        def actual_decorator[**T, U](func: Callable[T, Awaitable[U]]) -> Callable[T, Awaitable[U]]:
            @functools.wraps(func)
            async def wrapper(*args, **kwargs) -> U:
                await _print(end=t.black_on_white)
                await _print(end='-' * 3)
                await _print(end=' ')
                await _print(end=func.__name__)
                await _print(end=t.red)
                await _print(end=" (module: ")
                await _print(end=t.black)
                await _print(end=dunder_name)
                await _print(end=t.red)
                await _print(end=') ')
                await _print(end=t.black)
                await _print(end='-' * 3)
                await _print(t.normal)
                try:
                    return await func(*args, **kwargs)
                finally:
                    await _print()
            return wrapper
        return actual_decorator

    async_with_header.set_print = set_print

    return async_with_header
async_with_header = async_with_header()