import asyncio

this = ""

from g4f.client import AsyncClient

async def main():
    userin = input(">>")
    client = AsyncClient()
    stream = await client.chat.completions.create(
        model="mistral-7b",
        messages=[{"role": "user", "content": f"{userin}"}],
        stream=True,
        # Add any other necessary parameters
    )
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content or "", end="")

asyncio.run(main())
