from tools.future import Future
import asyncio


async def fetch_user_order():
    await asyncio.sleep(4)
    raise Exception('Logout failed: user ID is invalid')


async def print_text():
    (await asyncio.sleep(
        1,
        (lambda: print('Fetching user order...'))
    ))()


async def main():
    # # Отработают по очереди (Синхронный запуск)
    # await fetch_user_order(),
    # await print_text()

    # Асинхронный запуск (Вариант 1)
    await asyncio.gather(
        fetch_user_order(),
        print_text(),
    )

    # Асинхронный запуск (Вариант 2)
    # task1 = asyncio.create_task(fetch_user_order())
    # task2 = asyncio.create_task(print_text())
    #
    # await task1
    # await task2

asyncio.run(main())

# output:
# Fetching user order...
# Exception: Logout failed: user ID is invalid

#
# Future<void> fetchUserOrder() {
# // Imagine that this function is fetching user info but encounters a bug
#   return Future.delayed(Duration(seconds: 2),
#       () => throw Exception('Logout failed: user ID is invalid'));
# }
#
# void main() {
#   fetchUserOrder();
#   print('Fetching user order...');
# }