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
    def __init__(self, conn, id):
        self.conn = conn
        self.id = id
        conn.sendall(str.encode(str(id)))

    def send(self, data):
        self.conn.sendall(str.encode(data))

def broadcast(data, id):
    """Broadast data to all hosts"""
    for h in hostsClient:
        if h.id != id:
            h.send(data)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(4)
print("Waiting for a connection")

def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)
            print("data : " + str(data))
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                print("no data")
                break
            else:
                arr = reply.split(":")
                id = int(arr[0])
                broadcast(reply, id)

        except Exception as e:
            print("exception: " + str(e))
            break

    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    if hosts.count(addr) == 0:
        hosts.append(addr)
        id = hosts.index(addr)
        hostsClient.append(Client(conn, id))
        conn.sendall(str.encode(str(id)))
        
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))


