from vidstream import StreamingServer
import threading

print('[+] Waiting for screen...')

receiver = StreamingServer('127.0.0.1', 9999) # Mettez le même IP et port que le client

t = threading.Thread(target=receiver.start_server)
t.start()