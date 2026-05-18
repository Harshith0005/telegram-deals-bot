import asyncio
import os
import aiohttp
from telethon import TelegramClient, events

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
N8N_WEBHOOK = os.environ.get('N8N_WEBHOOK')

DEAL_CHANNELS = [
    'osmdhruva',
    'jsktechdealz',
    'tirupatideals',
    'KothimeerKattaaDeals',
    'ttsdeals',
    'telugutechtvdeals',
    'iamprasadtech',
    'TeluguTechworld'
]

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=DEAL_CHANNELS))
async def handler(event):
    message = event.message.message
    if not message:
        return
    
    lines = message.strip().split('\n')
    formatted = f"🔥🔥\n{message}"
    
    async with aiohttp.ClientSession() as session:
        await session.post(N8N_WEBHOOK, json={
            'message': formatted
        })
    print(f'Deal forwarded: {message[:50]}')

async def main():
    await client.start()
    print('Listening for deals...')
    await client.run_until_disconnected()

asyncio.run(main())
