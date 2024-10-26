from g4f.client import AsyncClient
from g4f.Provider import HuggingChat, HuggingFace
import asyncio
from bot_utilities.config_loader import load_current_language, config
import os

thehftokenusedonyouraccount = os.getenv("HF")

client = AsyncClient(
    provider=HuggingChat
)
'''
from huggingface_hub import AsyncInferenceClient

async def huggingchat(persona, history, search):
    print(history)
    model_id="mistralai/Mistral-Nemo-Instruct-2407"
    client = AsyncInferenceClient(api_key=thehftokenusedonyouraccount)

    search_result = f"Search_Results: {search}" if search is not None else ""

    messages = [
        { "role": "system", "content": persona },
	    *history,
#        {"role": "assistant", "search": "result", "content": search_result}
    ]
    output = await client.chat.completions.create(
        model=model_id, 
        messages=messages,
        temperature=0.5,
        top_p=0.7
    )

    return output.choices[0].message.content

'''
async def huggingchat(persona, history, search):
    search_result = search if search is not None else "search results is disabled"
    messages = [
        {"role": "system", "name": "instructions", "content": persona},
        *history,
        {"role": "assistant", "search": "result", "content": search_result}

    ]
    response = await client.chat.completions.create(
        #model=config['GPT_MODEL'],
        model="mistral-nemo",
        messages=messages
    )
    message = response.choices[0].message.content
    return message


print("using g4f!!")
