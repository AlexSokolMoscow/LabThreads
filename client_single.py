import aiohttp
import asyncio
import time


async def create(number):
    data = {
        "org_name": "sampleName",
        "date": "21.04.2023",
        "product_list": [[f"Product{number}", 1, number*10]]
    }
    async with aiohttp.ClientSession() as session:
        async with session.post("http://localhost:8080/add_item", json=data) as res:
            return await res.read()


async def main():
    tasks = []
    start_time = time.time()
    for number in range(4):
        tasks.append(asyncio.create_task(create(number)))
    result = await asyncio.gather(*tasks)
    end_time = time.time()
    print("Время работы программы :", end_time - start_time)
    tasks.clear()

asyncio.run(main())
