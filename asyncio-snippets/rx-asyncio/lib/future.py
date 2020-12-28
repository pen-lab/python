from asyncio import Future as _Future

from typing import Generic, TypeVar

T = TypeVar('T')


class Future(_Future, Generic[T]):
    pass
