import asyncio
import os
from telethon import TelegramClient, events

API_ID = os.environ.get('API_ID')
API_HASH = os.environ.get('API_HASH')
BOT_TOKEN = os.environ.get('BOT_TOKEN')
CHANNEL = os.environ.get('CHANNEL')
N8N_WEBHOOK = os.environ.get('N8N_WEBHOOK')

client = TelegramClient('session', API_ID, API_HASH)

DEAL_CHANNELS = [
    'dealsdhamaka',
    'lootdeals',
    'amazonindiadeals',
    'flipkartoffers',
    'indiadealshunters'
]

@client.on(events.NewMessage(chats=DEAL_CHANNELS))
async def handler(event):
    message = event.message.message
    import aiohttp
    async with aiohttp.ClientSession() as session:
        await session.post(N8N_WEBHOOK, json={
            'message': message,
            'chat': event.chat.username
        })

async def main():
    await client.start()
    print('Listening for deals...')
    await client.run_until_disconnected()

asyncio.run(main())
