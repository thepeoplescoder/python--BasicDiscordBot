from typing import Self
from typing import Any
from typing import TypedDict
from typing import ClassVar
from typing import TypeGuard
from typing import TypeVar
from typing import Protocol

from collections.abc import Coroutine
from collections.abc import Buffer
from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Awaitable

from asyncio import Server

from zlib import _Decompress as ZlibDecompressObject

from .servers import push

PrintCoroutineFunction = Callable[..., Coroutine[Any, Any, None]]

class ServerManagerDict(TypedDict):
    push: push.ServerManager

# enforce_type ############################################
def enforce_type[T](obj: Any, _type: type[T]) -> T:
    """Raises an exception if the given object does not match the given type,
    otherwise returns the object."""
    if isinstance(obj, _type):
        return obj
    raise TypeError(f"Value {obj} must be of type {_type}.  Please check your code.")

