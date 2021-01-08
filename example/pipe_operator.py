import asyncio

import aioreactive as rx
from aioreactive.subject import AsyncMultiSubject
from aioreactive.observers import AsyncAnonymousObserver



async def main():

    async def print_(num: int) -> None:
        print(f'Num: {num}')

    async def add_five(num: int) -> rx.AsyncObservable[int]:
        # return rx.single(num + 2)
        return num + 5

    stream: AsyncMultiSubject = AsyncMultiSubject[int]()


    xs: rx.AsyncObservable = rx.pipe(
        stream,
        rx.map_async(add_five),
    )
    await xs.subscribe_async(
        AsyncAnonymousObserver(asend=print_)
    )
    await stream.asend(1)
    await stream.asend(10)


asyncio.run(main())

