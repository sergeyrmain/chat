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


def send_message(client, message):
    message = message.encode(FORMAT)
    client.send(message)


def receive_message(client):
    message = client.recv(BUFFER_SIZE).decode(FORMAT)
    return message


def start():
    user_input = input('Would you like to connect to the server? (y/n): ')
    if user_input.lower() != 'y':
        return

    connection = connect()
    while True:

        message = input('Enter a message: (q to quit) ')
        if message.lower() == 'q':
            break
        send_message(connection, message)

    send_message(connection, DISCONNECT_MESSAGE)


start()
