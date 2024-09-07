from g4f.client import AsyncClient
from g4f.Provider import HuggingChat, HuggingFace
import asyncio
from bot_utilities.config_loader import load_current_language, config

client = AsyncClient(
    provider=HuggingChat
)


async def huggingchat(persona=str, history=str):
    messages = [
        {"role": "system", "persona": "name", "content": persona},
        *history,
    ]
    response = await client.chat.completions.create(
        model=config['GPT_MODEL'],
        messages=messages
    )
    message = response.choices[0].message.content
    return message

print("using g4f!!")