import asyncio
import os
from openai import AsyncClient
import dotenv
history = []

dotenv.load_dotenv()

key = os.getenv("CHIMERA_GPT_KEY")
#print(key)

with open("instructions/avernus.txt", "r") as avernus:
    mesa = avernus.read()

client = AsyncClient(api_key=f"{key}", base_url="https://api.naga.ac/v1")

async def main(things):
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"{mesa}"},
            *things,
            ],
    )
    cht = response.choices[0].message.content
    history.append({"role": "assistant", "content": f"{cht}"})
    print(cht)
    return cht


while True:
    user = input ("\n>>")
    history.append({"role": "user", "content": f"{user}"})
    asyncio.run(main(things=history))

