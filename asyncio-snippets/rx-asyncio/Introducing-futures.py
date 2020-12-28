from tools.future import Future
import asyncio


def fetch_user_order() -> Future[str]:
    return asyncio.sleep(2, 'Large Latte')


async def main():
    f = fetch_user_order()
    print('Fetching user order...')

    print(await f)

asyncio.run(main())

#output:
# Fetching user order...
# Large Latte