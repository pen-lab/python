from typing import List

import asyncio
from asyncio import Future, Task


# async def check_user_exists(user_id: int) -> bool:
#     async with aiohttp.ClientSession() as session:
#         url = f'https://example.org/users/{user_id}'
#         async with session.head(url) as resp:
#             print(user_id, resp.status == 200)
#             return resp.status == 200


async def check_user_exists(user_id: int) -> int:
    await asyncio.sleep(12 - user_id)
    print(f'check_user_exists: {user_id}')
    return user_id


async def main():
    future: Future = asyncio.get_running_loop().create_future()
    tasks: List[Task] = []
    executing: int = 0

    def cb(task: Task):
        nonlocal executing
        executing -= 1
        tasks.append(task)
        if executing == 0:
            future.set_result([task.result() for task in tasks])

    for i in range(10):
        task = asyncio.create_task(check_user_exists(i))
        task.add_done_callback(cb)
        executing += 1


    await future
    print(future.result())

asyncio.run(main())


async def sync_main():
    for i in range(10):
        print(await check_user_exists(i))

asyncio.run(sync_main())


async def coros_main():
    coros = (
        check_user_exists(i)
        for i in range(10)
    )
    # return coros

    resutls = await asyncio.gather(*coros) #<coroutine object coros_main at 0x7fc686e6dec0>
    print(resutls)

asyncio.run(coros_main())

