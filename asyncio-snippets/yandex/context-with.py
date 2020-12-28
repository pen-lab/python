import asyncio


class TransactionCtx:
    def __init__(self, conn):
        self.conn = conn

    async def __aenter__(self):
        await self.conn.execute('Begin')
        print('entering context')
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        command = 'ROLLBACK' if exc_val else 'COMMIT'
        await self.conn.execute(command)
        print('exiting context')


class Connect:
    def __init__(self, delay: int):
        self.delay = delay

    def raise_err(self):
        raise RuntimeError

    async def execute(self, command):
        await asyncio.sleep(self.delay)
        print(f'conn: {command}')


async def main():

    async def trans(conn):
        async with TransactionCtx(conn) as transaction:
            await asyncio.sleep(2)
            conn.raise_err()
            print('transaction')

    async def raise_err(conn: Connect):
        await asyncio.sleep(2)
        print('ok')
        # conn.raise_err()

    conn = Connect(4)

    await asyncio.gather(
        trans(conn),
        raise_err(conn)
    )
    print('completed')

asyncio.run(main())
