import socket
import threading


class Client:
    PORT = 8000
    SERVER = ''
    ADDRESS = (SERVER, PORT)
    FORMAT = 'utf-8'
    BUFFER_SIZE = 1024

    def __init__(self, name):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 , tcp
        self.client_socket.connect(self.ADDRESS)
        self.messages = []
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()
        self.send_messages(name)
        self.lock = threading.Lock()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(self.BUFFER_SIZE).decode(self.FORMAT)
                self.lock.acquire()
                self.messages.append(message)
                self.lock.release()
            except Exception as e:
                print(f'Error at receive_messages: {e}')
                break

    def send_messages(self, message):
        try:
            self.client_socket.send(bytes(message, self.FORMAT))
            if message == bytes(f"{quit}", self.FORMAT):
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
        self.send_messages(bytes(f"{quit}", self.FORMAT))