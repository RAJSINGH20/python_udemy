import asyncio

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    print(f"{name} is ready")


async def main():
    await asyncio.gather(
        brew("MAsala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai")
    )

asyncio.run(main())