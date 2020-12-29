from tools.future import Future
from typing import Callable
import asyncio


def raise_err():
    raise Exception('Cannot locate user order')


def fetch_user_order() -> Future[Callable]:
    # В качестве результата используется лямбда
    return asyncio.sleep(2, lambda: raise_err())


async def print_order_message() -> None:
    try:
        f: Callable = await fetch_user_order()
        print(f())
    except Exception as e:
        print(f'Exception: {e}')


async def main():
    await print_order_message()


asyncio.run(main())

# output:
# Exception: Cannot locate user order



# Future<void> printOrderMessage() async {
#   try {
#     var order = await fetchUserOrder();
#     print('Awaiting user order...');
#     print(order);
#   } catch (err) {
#     print('Caught error: $err');
#   }
# }
#
# Future<String> fetchUserOrder() {
#   // Imagine that this function is more complex.
#   var str = Future.delayed(
#       Duration(seconds: 4),
#       () => throw 'Cannot locate user order');
#   return str;
# }
#
# Future<void> main() async {
#   await printOrderMessage();
# }