import socket


class Network:

    def __init__(self, id):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = "192.168.1.25"
        self.port = 5555
        self.addr = (self.host, self.port)
        self.connect()
        self.id = id

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data):
        """
        :param data: str
        :return: str
        """
        try:
            msg = str(self.id) + ":" + data + ";"
            self.client.sendall(str.encode(msg))
            reply = self.client.recv(2048)
            return reply.decode("utf-8")
        except socket.error as e:
            print("error in network file : ")
            print(str(e))
            return str(e)
