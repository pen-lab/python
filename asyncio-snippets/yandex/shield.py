import asyncio
from asyncio import Task

async def coro() -> None:
    try:
        print('start')
        await asyncio.sleep(2)
        print('finished')
    finally:    # выполнится после tack.cancel()
        print('last canceled')


async def cancel(task: Task) -> None:
    await asyncio.sleep(0.5)
    task.cancel()

    print('task.cancel() called')

    try:
        await task
    except asyncio.CancelledError:
        print('task successfully cancelled')


async def main():
    task = asyncio.create_task(coro())

    asyncio.create_task(
        cancel(
            asyncio.shield(task)
        )
    )

    await asyncio.sleep(5)
    assert task.cancelled()

asyncio.run(main())
