import asyncio
from asyncio import Future


async def my_sleep(delay):
    loop = asyncio.get_running_loop()
    future: Future = loop.create_future()
    loop.call_later(delay, future.set_result, True)
    await future


async def main():
    loop = asyncio.get_running_loop()
    print(loop.time())
    await my_sleep(1)
    print(loop.time())


asyncio.run(main())