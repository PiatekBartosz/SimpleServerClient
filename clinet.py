import socket

# todo send json files
HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) # get host ipaddress
# SERVER = "192.168.1.203"
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_len = str(msg_len).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)

send("test message")
send(DISCONNECT_MESSAGE)