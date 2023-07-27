import socket
from .settings import settings


class ManipulatorClient:
    def __init__(self):
        self.host = settings.HOST_TCP
        self.port = settings.PORT_TCP

    def send(self, result):
        result = f'{result.created_at},{result.status}'

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect:
            connect.connect((self.host, self.port))
            connect.sendall(result.encode())
