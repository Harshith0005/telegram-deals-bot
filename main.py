import asyncio
import os
import aiohttp
from telethon import TelegramClient, events

API_ID = int(os.environ.get('API_ID'))
API_HASH = os.environ.get('API_HASH')
N8N_WEBHOOK = os.environ.get('N8N_WEBHOOK')

DEAL_CHANNELS = [
    'lootdeals',
    'dealsdhamaka',
    'amazonindiadeals',
    'flipkartoffers',
    'IndianDealHunters'
]

client = TelegramClient('session', API_ID, API_HASH)

@client.on(events.NewMessage(chats=DEAL_CHANNELS))
async def handler(event):
    message = event.message.message
    if not message:
        return
    async with aiohttp.ClientSession() as session:
        await session.post(N8N_WEBHOOK, json={
            'message': message,
            'channel': event.chat.username
        })
    print(f'Deal sent to n8n: {message[:50]}')

async def main():
    await client.start()
    print('Bot is running and listening for deals...')
    await client.run_until_disconnected()

asyncio.run(main())
