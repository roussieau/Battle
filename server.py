import socket
from _thread import *
import sys

hosts = []
hostsClient = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '0.0.0.0'
port = 5555

server_ip = socket.gethostbyname(server)

class Client: 
    def __init__(self, conn):
        self.conn = conn

    def send(self, data):
        self.conn.sendall(str.encode(data))

def broadcast(data):
    """Broadast data to all hosts"""

    for h in hostsClient:
        h.send(data)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(4)
print("Waiting for a connection")

def threaded_client(conn):
    conn.send(str.encode("Hello"))
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                conn.close()
                break
            else:
                broadcast(reply)

        except Exception as e:
            print("exception: " + str(e))
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    hostsClient.append(Client(conn))
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))
