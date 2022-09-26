import socket
import threading


from server_v2.client_obj import ClientObject
from server_v2.settings import settings


connected_clients = []

SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 , tcp
SERVER.bind((settings.SERVER, settings.PORT))


def broadcast(message, name):
    for client in connected_clients:
        current_client = client.client
        if name:
            current_client.send(bytes(f"{name}: {message}", settings.FORMAT))
        else:
            current_client.send(bytes(message, settings.FORMAT))


def handle_client(current_client):
    name = current_client.client.recv(settings.BUFFER_SIZE).decode(settings.FORMAT)
    current_client.set_name(name)
    message = f'{name} has joined the chat'
    broadcast(message, '')
    while True:
        try:
            message = current_client.client.recv(settings.BUFFER_SIZE).decode(settings.FORMAT)
            if not message:
                break
            if message == '{quit}':
                # current_client.client.send(bytes(f"{quit}", FORMAT))
                current_client.client.close()
                connected_clients.remove(current_client)
                broadcast(f'{name}: left the chat....', '')
                print(f'{name} has left the chat')
                break

            else:
                broadcast(message, name)
                print(f'{name}: {message}')



        except Exception as e:
            print(f'Error at handle_client: {e}')
            break


def wait_for_connections():
    while True:
        try:
            client, address = SERVER.accept()
            current_client = ClientObject(address, client)
            connected_clients.append(current_client)
            print(f'New connection: {address}')
            threading.Thread(target=handle_client, args=(current_client,)).start()

        except Exception as e:
            print(f'Error at wait_for_connections: {e}')
            break

    print('Server crashed')


if __name__ == '__main__':
    SERVER.listen(5)  # the 5 is the number of connections that can be queued
    print('Waiting for connections...')
    # Creating a thread that will wait for connections to the server.
    ACCEPT_THREAD = threading.Thread(target=wait_for_connections)
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
