from tools.future import Future
from typing import Callable
import asyncio


def raise_err():
    raise Exception('Cannot locate user order')


def fetch_username() -> Future[Callable]:
    # В качестве результата используется лямбда
    return asyncio.sleep(2, lambda: 'tester')


def add_hello(username: str) -> str:
    return f'Hello {username}'


async def greet_user() -> Future[str]:
    res = await fetch_username()
    return add_hello(res())


def logout_user() -> Future[Callable]:
    import random
    action: Callable = None

    if random.randint(0, 5) == 2:
        action = lambda: raise_err()
    else:
        action = lambda: 'pen logout'

    return asyncio.sleep(2, action)


async def say_goodbye() -> Future[Callable]:
    try:
        res: Callable = await logout_user()
        return f'{res()}. Thanks, see you next time'
    except Exception as e:
        return f'Error: {e}'


async def main():
    print(await greet_user())
    print(await say_goodbye())


asyncio.run(main())

# output:
# Hello tester
# Error: Cannot locate user order


#
# // Part 1
# String addHello(String username){
#   return 'Hello $username';
# }
#
# // Part 2
# // You can call the provided async function fetchUsername()
# // to return the username.
# Future<String> greetUser() async {
#   var res = await fetchUsername();
#   return addHello(res);
# }
#
# // Part 3
# // You can call the provided async function logoutUser()
# // to log out the user.
# Future<String> sayGoodbye() async{
#   try{
#     var res = await logoutUser();
#     return '$res Thanks, see you next time';
#   }
#   catch (e){
#     return 'Error ${e.toString()}';
#   }
# }
