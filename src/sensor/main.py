import asyncio
import random
import httpx
from multiprocessing import Pool
import datetime as datetime
import schemas


class Controller:

    async def send(self):
        data_serializer = schemas.ControllerSchema(
            created_at=datetime.datetime.now(),
            payload=random.randint(0, 200)
        )

        response = httpx.post('http://0.0.0.0:8000/', json=data_serializer)

        if response.status_code != 200:
            return None
        return response


def run():
    controller = Controller()
    asyncio.run(controller.send())


def main() -> None:
    while True:
        pool = Pool(processes=8)
        pool.apply_async(run)


if __name__ == '__main__':
    main()

