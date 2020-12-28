from tools.future import Future
import asyncio


def fetch_user_order() -> Future[str]:
    return asyncio.sleep(2, 'Large Latte')


async def print_order_message() -> None:
    print('Awaiting user order...')
    order = await fetch_user_order()
    print(f'You order is: {order}')


def count_seconds(s: int):
    return (
        asyncio.sleep(i, i)
        for i in range(s)
    )


async def main():
    for i in asyncio.as_completed(
            (print_order_message(), *count_seconds(10))
    ):
        res = await i
        if res is not None:
            print(f'{res}')


asyncio.run(main())

# output:
# Awaiting user order...
# 0
# 1
# You order is: Large Latte
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

#
# Future < void > printOrderMessage() async {
#     print('Awaiting user order...');
# var
# order = await fetchUserOrder();
#
# print('Your order is: $order');
# }
#
# Future < String > fetchUserOrder()
# {
# // Imagine
# that
# this
# function is more
# complex and slow.
# return Future.delayed(Duration(seconds: 2), () = > 'Large Latte');
# }
#
# Future < void > main() async {
# countSeconds(4);
# await printOrderMessage();
# }
#
# // You
# can
# ignore
# this
# function - it
# 's here to visualize delay time in this example.
# void
# countSeconds(int
# s) {
# for (var i = 1; i <= s; i++) {
#     Future.delayed(Duration(seconds: i), () = > print(i));
# }
# }