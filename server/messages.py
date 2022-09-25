import socket

PORT = 8000
SERVER = ''
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
BUFFER_SIZE = 1024


def connect():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 , tcp
    client.connect(ADDRESS)
    return client


def start():
    connection = connect()
    while True:
        message = connection.recv(BUFFER_SIZE).decode(FORMAT)
        print(message)


start()
