import asyncio
from concurrent.futures import ProcessPoolExecutor

def Encrypt(data):
    return f"lock {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool , Encrypt , "Credit card 1234")
        print(result)


if __name__ == "__main__":
    asyncio.run(main())