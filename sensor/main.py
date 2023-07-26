import httpx
from sensor.schemas import ControllerSchema


class Controller:

    async def send(self):
        data_serializer = ControllerSchema(
            status='up',
            payload=42
        )
        response = httpx.post('http://127.0.0.1:8000/', json=data_serializer)

        if response.status_code != 200:
            return None
        return response


class Work:

    def run(self):
        controller = Controller()
        controller.send()
