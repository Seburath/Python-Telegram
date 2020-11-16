import asyncio
import time
import datetime
from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon import utils


msgs = []
translator_msgs = []

async def send(user, msg):
    await client.send_message(user, msg)

async def receive(user):
    async for msg in client.iter_messages(user, limit=2):
        msgs.append(msg)
    return msgs


if __name__ ==  '__main__':
    phone = '+593988306013'
    api_id = 655586
    api_hash = '4bc685e77f57d5b2bc92f7eef3af5b8f'

    myuser = 'seburath'
    translator = 'YTranslateBot'

    client = TelegramClient('session1', api_id, api_hash).start(phone)
    client.start()

    loop = asyncio.get_event_loop()

    while True:
        time.sleep(2)
        
        msgs = []
        msgs = loop.run_until_complete(receive(myuser))
        is_recent = True

        if msgs[-1].message == 't' and is_recent:

            loop.run_until_complete(send(translator, msgs[-2].message))
            print('translating:' + msgs[-1].message)
            time.sleep(1)
            translator_msgs = []
            translator_msgs = loop.run_until_complete(receive(translator))

            if translator_msgs[-2].message:
                loop.run_until_complete(send(myuser, translator_msgs[-2].message))
