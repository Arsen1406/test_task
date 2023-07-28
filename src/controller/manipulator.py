

class ManipulatorClient:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 50000

    def send(self, result):
        import socket
        result = f'{result.created_at},{result.status}'

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect:
            connect.connect((self.host, self.port))
            connect.sendall(result.encode())
