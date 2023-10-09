from vidstream import ScreenShareClient
import threading

print('[+] Sharing screen..')
sender = ScreenShareClient('127.0.0.1', 9999) # Mettez l'adresse IP et le port du serveur

t = threading.Thread(target=sender.start_stream)
try:
    t.start()
except:print('Stop')