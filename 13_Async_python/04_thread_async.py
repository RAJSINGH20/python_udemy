import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


# Function to check stock
def check_stock(item):
    print(f"Checking {item} in stores...")
    time.sleep(2)
    return f"{item} stock: 42"


# Main asynchronous function
async def main():
    # Get the current event loop
    loop = asyncio.get_running_loop()

    # Create a thread pool
    with ThreadPoolExecutor() as pool:
        # Run the blocking function in a separate thread
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)


# Start the event loop
asyncio.run(main())