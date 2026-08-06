import asyncio
import aiohttp


# Function to fetch a URL asynchronously
async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


# Main asynchronous function
async def main():
    urls = ["https://en.wikipedia.org/wiki/Food"] * 3

    # Create an HTTP session
    async with aiohttp.ClientSession() as session:

        # Create a list of tasks
        tasks = [fetch_url(session, url) for url in urls]

        # Run all tasks concurrently
        # task = [t1 , t2 , t3]
        await asyncio.gather(*tasks)


# Start the event loop
asyncio.run(main())