import asyncio


async def trigger(position):
    await asyncio.sleep(position)
    if position == 3:
        raise RuntimeError('Boom!')

    print(f'{position} is ok')


async def russian_roulette() -> None:
    coros = (trigger(i) for i in range(8))

    try:
        await asyncio.gather(*coros)
        # await asyncio.gather(*coros, return_exceptions=False)
    except RuntimeError as e:
        print(e)

    await asyncio.sleep(10)

asyncio.run(russian_roulette())
