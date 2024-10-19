import asyncio

this = ""

from g4f.client import AsyncClient

async def main(things):
    client = AsyncClient()
    stream = await client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{things}"}],
        stream=True,
        # Add any other necessary parameters
    )
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content or "", end="")

while True:
    user = input ("\n>>")
    asyncio.run(main(things=user))

