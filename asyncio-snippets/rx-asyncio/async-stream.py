from tools.future import Future
from typing import Callable
import asyncio
import aioreactive as rx
from aioreactive import AsyncObservable as Stream


async def sum_stream(stream: Stream[int]) -> Future[int]:
    sum: int = 0
    obv = rx.AsyncIteratorObserver(stream)
    async for result in obv:
        sum += result
    return sum


def count_stream(to: int) -> Stream[int]:
    return rx.from_iterable(range(to))


async def main():
    stream = count_stream(10)
    sum_ = await sum_stream(stream)
    print(sum_)


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







