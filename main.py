import httpx
import asyncio


async def fetch_store(client, url):
    resp = await client.get(url)
    products = resp.json()
    return url, products['products'][0]['title']


async def main():
    with open('stores.txt', 'r') as f:
        urls = [line.strip() for line in f.readlines()]

    async with httpx.AsyncClient() as client:
        tasks = []

        for url in urls:
            tasks.append(asyncio.create_task(fetch_store(client, url)))

        results = await asyncio.gather(*tasks)

    return results


if __name__ == '__main__':
    results = asyncio.run(main())
    print(results)
