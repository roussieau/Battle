import socket
from _thread import *
import sys

hosts = []
hostsClient = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = 'localhost'
port = 5555

server_ip = socket.gethostbyname(server)

class Client: 
    def __init__(self, conn, id):
        self.conn = conn
        self.id = id
        conn.sendall(str.encode("c:" + str(id)))

    def send(self, data):
        self.conn.sendall(str.encode(data))

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(4)
print("Waiting for a connection")

pos = ["0:50,50", "1:100,100"]
def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                print("no data")
                break
            else:
                print("Recieved: " + reply)
                #arr = reply.split(":")
                #id = int(arr[0])
                #pos[id] = reply

                #if id == 0: nid = 1
                #if id == 1: nid = 0

                #reply = pos[nid][:]

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


