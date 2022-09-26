from client import Client
import time
import threading



c1 = Client('Sergio')
c2 = Client('Dave')


def update_messages():
    messages = []
    run = True
    while run:
        time.sleep(0.1)
        messages = c1.get_messages()
        messages.extend(messages)
        for message in messages:
            print(message)
            if message == '{quit}':
                run = False
                break


threading.Thread(target=update_messages).start()


c1.send_messages('Hello')
time.sleep(2)
c2.send_messages('how are you?')
time.sleep(2)
c1.send_messages('I am fine')
time.sleep(2)
c2.send_messages('I am fine too')
time.sleep(2)
c1.send_messages('bye')
time.sleep(2)
c2.send_messages('bye')
time.sleep(2)
c1.disconnect()
time.sleep(2)
c2.disconnect()