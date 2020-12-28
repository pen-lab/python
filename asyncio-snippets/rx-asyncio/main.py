from tools.future import Future
import asyncio



def fetch_user_order() -> Future[str]:
    return asyncio.sleep(4, 'Large Latte')


# def create_call_later(loop, i: int, future, ):
#     loop.call_later(i, f, future)

def count_seconds(s: int):
    return (
        asyncio.sleep(i, i)
        for i in range(s)
    )

async def main():
    # # Отработают по очереди (Синхронный запуск)
    # await fetch_user_order(),
    # await print_text()

    # Асинхронный запуск (Вариант 1)

    f = await asyncio.gather(
        fetch_user_order(),
        *count_seconds(10)
    )

    [print(i) for i in f]

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




# Future<void> printOrderMessage() async {
#   print('Awaiting user order...');
#   var order = await fetchUserOrder();
#   print('Your order is: $order');
# }
#
# Future<String> fetchUserOrder() {
#   // Imagine that this function is more complex and slow.
#   return Future.delayed(Duration(seconds: 4), () => 'Large Latte');
# }
#
# Future<void> main() async {
#   countSeconds(4);
#   await printOrderMessage();
# }
#
# // You can ignore this function - it's here to visualize delay time in this example.
# void countSeconds(int s) {
#   for (var i = 1; i <= s; i++) {
#     Future.delayed(Duration(seconds: i), () => print(i));
#   }
# }