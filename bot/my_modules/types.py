from os import PathLike
from socket import socket

from typing import Self
from typing import Any
from typing import TypedDict
from typing import ClassVar
from typing import TypeGuard
from typing import TypeVar
from typing import Protocol
from typing import TypeAlias
from typing import Optional

from collections.abc import Mapping
from collections.abc import Coroutine
from collections.abc import Buffer
from collections.abc import Callable
from collections.abc import Iterator
from collections.abc import Awaitable
from collections.abc import Sequence

from asyncio import Server
from asyncio.streams import StreamReader
from asyncio.streams import StreamWriter

StrPath:                TypeAlias = str | PathLike[str]
PrintCoroutineFunction: TypeAlias = Callable[..., Awaitable[None]]
ConnectionDict:         TypeAlias = dict[tuple[StreamReader, StreamWriter], socket]

# enforce_type ############################################
def enforce_type[T](obj: Any, _type: type[T]) -> T:
    """Raises an exception if the given object does not match the given type,
    otherwise returns the object."""
    if isinstance(obj, _type):
        return obj
    raise TypeError(f"Value {obj} must be of type {_type}.  Please check your code.")