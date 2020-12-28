import asyncio


async def check_user_exists(user_id: int) -> int:
    await asyncio.sleep(12 - user_id)
    print(f'check_user_exists: {user_id}')
    return user_id


async def main():

    tasks = [
        asyncio.create_task(check_user_exists(i))
        for i in range(10)
    ]

    # Задачи выполненные за 6 мс
    # done, pending = await asyncio.wait(tasks, timeout=6)

    # До первой выполненной задачи
    done, pending = await asyncio.wait(
        tasks,
        return_when=asyncio.FIRST_COMPLETED
    )

    print(done, pending)

asyncio.run(main())



## asyncio.as_complated - в порядке выполнения


async def delayed_result(delay):
    if delay == 2:
        return 2
    return await asyncio.sleep(10 - delay, delay)


async def main_as_completed():
    tasks = [
        delayed_result(i)
        for i in range(10)
    ]

    for earliest in asyncio.as_completed(tasks):
        result = await earliest
        print(result)

asyncio.run(main_as_completed())

## Все задачи запущенные в цикле


# async def check_user_exists(user_id: int) -> int:
#     await asyncio.sleep(12 - user_id)
#     print(f'check_user_exists: {user_id}')
#     return user_id


async def main_all_task():
    coros = (
        check_user_exists(i)
        for i in range(10)
    )

    asyncio.gather(*coros)
    await asyncio.sleep(2)
    tasks = asyncio.all_tasks()

    print(type(tasks))
    print(tasks)

asyncio.run(main_all_task())