import asyncio
import threading
import time

def backgroundWorker():
    while True:
        time.sleep(1)
        print(f" logging the System Health")

async def Fetch_Order():
    await asyncio.sleep(3)
    print("order fetched")

threading.Thread(target = backgroundWorker, daemon=True).start()

asyncio.run(Fetch_Order())