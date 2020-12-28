import asyncio


async def ticker(delay, to):
    for i in range(to):
        yield i
        await asyncio.sleep(delay)


async def main():
    resutls = [
        (i, j)
        async for i in ticker(1, 5)
        async for j in ticker(1, 5)
        if not i % 2 and j % 2
    ]

    print(resutls)

asyncio.run(main())