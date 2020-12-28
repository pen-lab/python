import asyncio
from .lib.future import Future


def fetch_user_order() -> Future[str]:
    # return asyncio.sleep(2, 'Large Latte')
    return asyncio.sleep(2, 'Large Latte')


def create_order_message() -> str:
    order = fetch_user_order()
    return f'You order is {order}'


def main():
    print(create_order_message())

main()

#output: You order is <coroutine object sleep at 0x7f0eff96d7c0>