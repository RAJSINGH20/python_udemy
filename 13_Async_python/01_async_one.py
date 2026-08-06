import asyncio

async def brew_chai():
    print("brewing Chai...")
    await asyncio.sleep(2)
    print("chai Ready..")


asyncio.run(brew_chai())