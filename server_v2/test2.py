from client import Client
import time
import threading



c1 = Client('Sergio')
c2 = Client('Dave')


def update_messages():
    msgs = []
    while True:
        time.sleep(0.1)
        messages = c1.get_messages()
        msgs.extend(messages)
        for msg in msgs:
            print(msg)
            if msg == 'quit':
                break


threading.Thread(target=update_messages).start()


c1.send_messages('Hello')
time.sleep(1)
c2.send_messages('how are you?')
time.sleep(1)
c1.send_messages('I am fine')
time.sleep(1)
c2.send_messages('I am fine too')
time.sleep(1)
c1.send_messages('bye')
time.sleep(1)
c2.send_messages('bye')
time.sleep(1)
c1.disconnect()
c2.disconnect()