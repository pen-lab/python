from asyncio import Future

from typing import Generic, TypeVar

T = TypeVar('T')


class Future(Future, Generic[T]):
    pass
