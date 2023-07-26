from loguru import logger


class Manipulator:

    def __init__(self, response):
        self.response = response

    async def output(self):
        data = self.response.json()
        logger.info(
            f'status - {data.get("status")}, time - {data.get("datatime")}'
        )

