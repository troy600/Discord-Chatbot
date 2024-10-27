from g4f.client import Client
from g4f.Provider import HuggingChat, HuggingFace
import asyncio
from bot_utilities.config_loader import load_current_language, config
import os

thehftokenusedonyouraccount = os.getenv("HF")

modelu = config['G4F_MODEL']

client = Client(
    provider=HuggingChat
)

async def huggingchat(persona, history, search):
#    search_result = search if search is not None else "search results is disabled"
    messages = [
        {"role": "system", "name": "instructions", "content": persona},
        *history,
#        {"role": "assistant", "search": "result", "content": search_result}

    ]
    response = await client.chat.completions.async_create (
        #model=config['GPT_MODEL'],
        model=modelu,
        messages=messages
    )
    message = response.choices[0].message.content
    return message


#print("using g4f!!")
