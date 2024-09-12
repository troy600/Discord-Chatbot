from g4f.client import AsyncClient
from g4f.Provider import HuggingChat, HuggingFace
import asyncio
from bot_utilities.config_loader import load_current_language, config
client = AsyncClient(
    provider=HuggingChat
)

async def huggingchat(persona, history, search):
    search_result = search if search is not None else "search results is disabled"
    messages = [
        {"role": "system", "name": "instructions", "content": persona},
        *history,
        {"role": "assistant", "search": "result", "content": search_result}

    ]
    response = await client.chat.completions.create(
        model=config['GPT_MODEL'],
        #model="mixtral-x87b",
        messages=messages
    )
    message = response.choices[0].message.content
    return message

print("using g4f!!")