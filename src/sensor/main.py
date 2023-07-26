import asyncio
import random

import httpx
from schemas import ControllerSchema
from multiprocessing import Pool
import datetime as datetime


class Controller:

    async def send(self):
        data_serializer = ControllerSchema(
            created_at=datetime.datetime.now(),
            payload=random.randint(0, 200)
        )
        response = httpx.post('http://127.0.0.1:6000/', json=data_serializer)

        if response.status_code != 200:
            return None
        return response


class Work:

    def run(self):
        controller = Controller()
        asyncio.run(controller.send())


def main() -> None:
    while True:
        work = Work()
        pool = Pool(processes=8)
        pool.apply_async(work.run)


if __name__ == '__main__':
    main()

