import threading
import time

def moniter():
    while True:
        print(f"Monitoring the temperature...")
        time.sleep(2)

threading.Thread(target=moniter,daemon=True).start()
print(f"main program done !")