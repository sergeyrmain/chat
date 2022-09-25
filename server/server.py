import socket
import threading

PORT = 8000
SERVER = ''
ADDRESS = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT'
BUFFER_SIZE = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 , tcp
server.bind(ADDRESS)

clients = set()
clients_lock = threading.Lock()  # locking all the other threads from modifying anything to do with the client's data, while this thread is running. will be unlocked when the thread is done


def handle_client(connection, address):
    print(f'New connection: {address}')
    try:
        while True:  # will run as long as the client is connected
            message = connection.recv(BUFFER_SIZE).decode(FORMAT)
            if not message:
                break
            if message == DISCONNECT_MESSAGE:
                break

            print(f'{address} sent: {message}')
            with clients_lock:
                for client in clients:
                    client.sendall(message.encode(FORMAT))
    except Exception as e:
        print(f'Error: {e}')

    finally:
        with clients_lock:
            clients.remove(connection)
        connection.close()
        print(f'Connection closed: {address}')


def connection_start():
    print('Listening for connections...')
    server.listen()
    while True:
        try:
            connection, address = server.accept()  # infinitely trying to accept incoming connections
            with clients_lock:
                clients.add(connection)
            thread = threading.Thread(target=handle_client,
                                      args=(connection,
                                            address))  # create a new thread for each client-> to not block other clients to send messages
            thread.start()
        except Exception as e:
            print(f'Error: {e}')


def start():
    print('Starting server...')
    server.listen()
    while True:
        connection, address = server.accept()
        with clients_lock:
            clients.add(connection)
        thread = threading.Thread(target=handle_client,
                                  args=(connection,
                                        address))
        thread.start()


start()
