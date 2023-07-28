from loguru import logger


class ManipulatorServer:
    def __init__(self):
        self.host = '127.0.0.1'
        self.port = 50000

    def output(self):
        import socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connect:
            connect.bind((self.host, self.port))
            connect.listen()
            session, addr = connect.accept()

            while True:
                data = session.recv(1024)

                if not data:
                    break

                session.sendall(data)
                date, status = data.decode().split(',')
                logger.info(f'status - {status}, time - {date}')


if __name__ == '__main__':
    socket = ManipulatorServer()
    socket.output()
