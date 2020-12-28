import asyncio
import time


class Timer:
    def __init__(self, coro) -> None:
        self.coro = coro
        self.spend = 0

    def __await__(self):
        started = time.monotonic()
        result = yield from self.coro.__await__()
        self.spend = time.monotonic() - started
        return result


async def main():
    t = Timer(asyncio.sleep(1, 'test'))

    res = await t
    print(res)
    print(t.spend)
