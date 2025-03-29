# main_01.py
import asyncio

async def func1():
    print("func1: Start")
    await asyncio.sleep(2)  # Asynchronously wait for 2 seconds
    print("func1: End")

async def func2():
    print("func2: Start")
    await asyncio.sleep(1)  # Asynchronously wait for 1 second
    print("func2: End")

async def main():
    await asyncio.gather(func1(), func2())  # Run func1 and func2 concurrently

if __name__ == "__main__":
    asyncio.run(main())
# Run the script using: python main_01.py