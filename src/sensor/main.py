import asyncio
import random
import httpx
from multiprocessing import Pool
import datetime as datetime
import schemas

URL = 'http://web:8000/'


class Controller:

    async def send(self):
        status = 1
        down = 0
        up = 0

        for _ in range(1500):
            status_sensor = random.randint(0, 200)
            if status_sensor >= 100:
                down += 1
            else:
                up += 1

        all_result = down + up
        if down > all_result // 100 * 30:
            status = 0

        data_serializer = schemas.ControllerSchema(
            created_at=datetime.datetime.now(),
            payload=status
        )

        response = httpx.post(URL, data=data_serializer.json())

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

