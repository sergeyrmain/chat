import socket
import threading

from server_v2.settings import settings


class Client:

    def __init__(self, name):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 , tcp
        self.client_socket.connect((settings.SERVER, settings.PORT))
        self.messages = []
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_messages(name)
        self.lock = threading.Lock()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(settings.BUFFER_SIZE).decode(settings.FORMAT)
                self.lock.acquire()
                self.messages.append(message)
                self.lock.release()
            except Exception as e:
                print(f'Error at receive_messages: {e}')
                break

    def send_messages(self, message):
        try:
            self.client_socket.send(bytes(message, settings.FORMAT))
            print('send_messages: ', message)
            if message == '{quit}':
                self.client_socket.close()
                return
        except Exception as e:
            print(f'Error at send_messages: {e}')
            self.client_socket.close()

    def get_messages(self):
        self.lock.acquire()
        messages_copy = self.messages[:]
        self.messages = []
        self.lock.release()
        return messages_copy

    def disconnect(self):
        self.send_messages('{quit}')



