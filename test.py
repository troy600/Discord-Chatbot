from openai import AsyncOpenAI
from g4f.client import AsyncClient
import os
from dotenv import load_dotenv # python-dotenv
import asyncio

print(load_dotenv())

client = AsyncOpenAI(api_key=os.getenv("CHIMERA_GPT_KEY"), base_url="https://api.naga.ac/v1/")

async def chatcompletion(mesg):
    msg = [{"role": "user", "content": mesg}]
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=msg,
    )

    return response.choices[0].message.content


def main():
    lsa = input("\n >>")
    print(asyncio.run(chatcompletion(mesg=lsa)))


main()