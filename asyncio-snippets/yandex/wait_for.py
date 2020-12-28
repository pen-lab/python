import asyncio


async def eternity() -> None:
    try:
        await asyncio.sleep(3600)
    except asyncio.CancelledError:
        print('i was cancelled')
        raise
    print('finished')


async def main() -> None:
    try:
        await asyncio.wait_for(eternity(), timeout=1.0)
    except asyncio.TimeoutError:
        print('timeout')

asyncio.run(main())