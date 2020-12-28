import asyncio


class Ticker:
    def __init__(self, delay, to):
        self.delay = delay
        self.i = 0
        self.to = to

    def __aiter__(self):
        return self

    async def __anext__(self):
        i = self.i
        if i >= self.to:
            raise StopAsyncIteration
        self.i += 1

        if i:
            await asyncio.sleep(self.delay)

        return i


async def main():

    async def ticker_1():
        async for i in Ticker(2, 3):
            print(f'Ticker 1: {i}')

    async def ticker_2():
        async for i in Ticker(4, 2):
            print(f'Ticker 2: {i}')

    await asyncio.gather(
        ticker_1(),
        ticker_2()
    )
    print('completed')

asyncio.run(main())
