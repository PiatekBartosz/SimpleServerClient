import socket 
import threading
import time
import json

HEADER = 64 # 1st massage to the server size
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # get host ipaddress
# SERVER = "192.168.1.203"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# this will be running for each thread
def handle_client(conn, addr):
    print("f[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        # reciving messange
        msg_length = conn.recv(HEADER).decode(FORMAT) # "blocking"
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")

        # sending text message
        msg = {
            "3-bit": {
                "count": 2,
                "bbox": [
                    {"no": 0, "x": 255, "y": 355},
                    {"no": 1, "x": -33, "y": 0}
                ]
            },

            "snickers": {
                "count": 1,
                "bbox": [
                    {"no": 0, "x": 255, "y": 355},
                ]
            }
        }
        send_msg = json.dumps(msg).encode()
        conn.send(send_msg)


    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept() # wait until new connection, store conn and address
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
