# import socket
# import threading
# import time
#
#
# PORT = 8000
# SERVER = ''
# ADDRESS = (SERVER, PORT)
# FORMAT = 'utf-8'
# BUFFER_SIZE = 1024
# messages = []
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # ipv4 , tcp
# client_socket.connect(ADDRESS)
#
#
# def receive_messages():
#     while True:
#         try:
#             message = client_socket.recv(BUFFER_SIZE).decode(FORMAT)
#             messages.append(message)
#             print(message)
#         except Exception as e:
#             print(f'Error: {e}')
#             break
#
#
# def send_messages(message):
#     try:
#         client_socket.send(bytes(message, FORMAT))
#         if message == bytes(f"{quit}", FORMAT):
#             client_socket.close()
#             return
#     except Exception as e:
#         print(f'Error: {e}')
#         client_socket.close()
#
#
# receive_thread = threading.Thread(target=receive_messages)
# receive_thread.start()
#

