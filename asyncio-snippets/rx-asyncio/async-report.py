from tools.future import Future
from typing import Callable
import asyncio


def fetch_role() -> Future[Callable]:
    # В качестве результата используется лямбда
    return asyncio.sleep(2, lambda: 'tester')


async def report_user_role():
    return f'User role: {(await fetch_role()) ()}'


def fetch_login_amount() -> Future[str]:
    return asyncio.sleep(0.5, '10')


async def report_logins() -> str:
    return f'Total number of logins: {await fetch_login_amount()}'


async def main():
    for i in asyncio.as_completed(
            (report_user_role(), fetch_login_amount())
    ):
        res = await i
        if res is not None:
            print(f'{res}')


asyncio.run(main())

# output:
# 10
# User role: tester


#
# Future<String> reportUserRole() async {
#   return 'User role: ${await fetchRole()}';
# }
#
# // Part 2
# // Implement reportLogins here
# // You can call the provided async function fetchLoginAmount()
# // to return the number of times that the user has logged in.
# Future<String> reportLogins() async {
#   return 'Total number of logins: ${await fetchLoginAmount()}';
# }
