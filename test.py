from openai import AsyncOpenAI
from g4f.client import AsyncClient
from g4f.Provider import HuggingChat
import os
from dotenv import load_dotenv # python-dotenv
import asyncio

print(load_dotenv())

client = AsyncOpenAI(api_key=os.getenv("CHIMERA_GPT_KEY"), base_url="https://api.naga.ac/v1/")
g4fclient = AsyncClient(provider=HuggingChat)

async def g4fmsg(message):
    msg = [{"role": "user", "content": message}]
    response = await g4fclient.chat.completions.create(
        model="mistral-7b",
        messages=msg
    )
    return response.choices[0].message.content

async def chatcompletion(mesg):
    msg = [{"role": "user", "content": mesg}]
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=msg,
    )

    return response.choices[0].message.content

lsa = input("\n >>")
print(asyncio.run(g4fmsg(message=lsa)))

'''
def main():
    lsa = input("\n >>")
    print(asyncio.run(chatcompletion(mesg=lsa)))
'''