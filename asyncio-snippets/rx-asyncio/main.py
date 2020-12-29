from tools.future import Future
from typing import Callable
import asyncio
import aioreactive as rx
from aioreactive import AsyncObservable as Stream


async def sum_stream() -> Future[None]:
    f = asyncio.get_running_loop().create_future()
    f.add_done_callback(lambda: print('Hello'))
    return asyncio.sleep(2, f)



def count_stream(to: int) -> Stream[int]:
    return rx.from_iterable(range(to))


async def main():
    await sum_stream()


asyncio.run(main())

# output:
# 45




# import 'dart:async';
#
# Future<int> sumStream(Stream<int> stream) async {
#   var sum = 0;
#   await for (var value in stream) {
#     sum += value;
#   }
#   return sum;
# }
#
# Stream<int> countStream(int to) async* {
#   for (int i = 1; i <= to; i++) {
#     yield i;
#   }
# }
#
# main() async {
#   var stream = countStream(10);
#   var sum = sumStream(stream);
#   print(await sum); // 55
# }
#







