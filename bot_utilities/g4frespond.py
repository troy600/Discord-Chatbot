from g4f.client import AsyncClient
from g4f.Provider import HuggingChat, HuggingFace
import asyncio
from bot_utilities.config_loader import load_current_language, config
from bot_utilities.ai_utils import search

client = AsyncClient(
    provider=HuggingChat
)


async def huggingchat(persona, history, search):
    messages = [
        {"role": "system", "name": "instructions", "content": persona},
        *history,
        {"role": "assistant", "search": "result", "content": search}

    ]
    response = await client.chat.completions.create(
        #model=config['GPT_MODEL'],
        model="mixtral-x87b",
        messages=messages
    )
    message = response.choices[0].message.content
    return message

print("using g4f!!")