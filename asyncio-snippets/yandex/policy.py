
# Level: hard

# asyncio.WindowsProactorEventLoopPolicy
# asyncio.ProactorEventLoop
# asyncio.SelectorEventLoop

import asyncio

asyncio.set_event_loop_policy(
    asyncio.WindowsProactorEventLoopPolicy()
)

# github: uvloop

#_run_once()

import selectors # посмотреть

## Запуск блокируемого кода

from concurrent import futures
# asyncio.WindowsProactorEventLoopPolicy
# asyncio.ProactorEventLoop
# asyncio.SelectorEventLoop

import asyncio

asyncio.set_event_loop_policy(
    asyncio.WindowsProactorEventLoopPolicy()
)

# github: uvloop

#_run_once()

import selectors # посмотреть

## Запуск блокируемого коtures

def blocking_io():
    with open('/dev/urandom', 'rb') as f:
        return f.read(100)


def cpu_bound():
    return sum(i * i for i in range(10 ** 7))


async def main():
    loop = asyncio.get_running_loop()

    resutl = await loop.run_in_executor(None, blocking_io)
    print('default thread pool', resutl)


    with futures.ThreadPoolExecutor() as pool:
        resutl = await loop.run_in_executor(pool, blocking_io)
        print('default thread pool', resutl)



    with futures.ProcessPoolExecutor() as pool:
        resutl = await loop.run_in_executor(pool, blocking_io)
        print('default process pool', resutl)

asyncio.run(main())
