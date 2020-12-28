import asyncio


async def ticker(delay, to):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


async def main():

    async def ticker_1():
        async for i in ticker(2, 3):
            print(f'Ticker 1: {i}')

    async def ticker_2():
        async for i in ticker(4, 2):
            print(f'Ticker 2: {i}')

    await asyncio.gather(
        ticker_1(),
        ticker_2()
    )
    print('completed')

asyncio.run(main())
