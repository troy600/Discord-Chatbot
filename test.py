import asyncio
from g4f.Provider import HuggingChat
history = []

from g4f.client import Client

async def main(things):
    client = Client(
        provider=HuggingChat,
    )
    response = await client.chat.completions.async_create(
        model="mistral-nemo",
        messages=[
            {"role": "system", "content": f"{mesa}},
            *things
            ],
    )
    cht = response.choices[0].message.content
    history.append({"role": "assistant", "content": f"{cht}"},)
    print(cht)
    return cht
    

while True:
    user = input ("\n>>")
    history.append({"role": "user", "content": f"{user}"},)
    asyncio.run(main(things=history))

