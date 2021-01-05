from aioreactive.types import T_contra

from tools.future import Future
from typing import Callable
import asyncio
import aioreactive as rx
from aioreactive import AsyncObservable as Stream
from aioreactive import AsyncObserver as Observer


def count_stream(to: int) -> Stream[int]:
    return rx.from_iterable(range(to))


class Print(Observer):

    async def asend(self, value: int) -> None:
        print(f'Print one: {value}')


class FilePrint(Observer):
    def __init__(self, path) -> None:
        super().__init__()
        self._path = path

    async def asend(self, value: int) -> None:
        with open(self._path, 'a+') as f:
            f.writelines([f'{value}\n'])


async def main():
    stream = rx.AsyncSubject()
    await stream.subscribe_async(Print())
    await stream.subscribe_async(FilePrint('numbers.txt'))
    await stream.asend(1)
    await asyncio.sleep(3)
    await stream.asend(2)


asyncio.run(main())
