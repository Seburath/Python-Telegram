import asyncio
import time
import datetime
from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon import utils

async def telelgram_response():
    await client.send_message(nickname, 'Recived on Telegram, executing order...')

async def telelgram_read():
    async for msg in client.iter_messages(nickname, limit=10):
        print(msg.id, msg.to_id.user_id, msg.date, msg.message)

if __name__ ==  '__main__':
    #from
    phone = '+593xxxxxxxxx'
    api_id = 666666
    api_hash = '4bc685e77f57d5bxxxxxxxxxx'
    #to
    nickname = 'jannasp'

    client = TelegramClient('session1', api_id, api_hash).start(phone)
    client.start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(telelgram_response())

    last_id = read('.last_id.txt')
    while True:
        time.sleep(1)
        loop.run_until_complete(telelgram_read())
        print(datetime.datetime.now())
