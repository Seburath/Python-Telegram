import asyncio
import time
import datetime
from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
from telethon import utils


def sleep():
    time.sleep(2)

myuser = 'seburath'
translator = 'YTranslateBot'
bot = 'Itemsy_Bot'

msgs = []
translator_msgs = []
bot_msgs = []

async def send(user, msg):
    await client.send_message(user, msg)

async def receive(user):
    async for msg in client.iter_messages(user, limit=2):
        if user == myuser:
            msgs.append(msg)
        if user == translator:
            translator_msgs.append(msg)
        if user == bot:
            bot_msgs.append(msg)
    if user == myuser:
        return msgs
    if user == translator:
        return translator_msgs
    if user == bot:
        return bot_msgs


if __name__ == '__main__':
    phone = '+593988306013'
    api_id = 655586
    api_hash = '4bc685e77f57d5b2bc92f7eef3af5b8f'

    client = TelegramClient('session1', api_id, api_hash).start(phone)
    client.start()

    loop = asyncio.get_event_loop()

    while True:
        sleep()

        msgs = []
        msgs = loop.run_until_complete(receive(myuser))

        is_recent = True

        if msgs[0].message == 't' and msgs[1].message != 't' and is_recent:

            loop.run_until_complete(send(translator, msgs[1].message))
            sleep()
            print('Translating: ' + msgs[1].message)

            translator_msgs = []
            translator_msgs = loop.run_until_complete(receive(translator))
            sleep()
            print('translator: ' + translator_msgs[0].message)

            if translator_msgs[0].message:
                loop.run_until_complete(send(myuser, translator_msgs[0].message))

        elif msgs[0].message.split(':')[0] != 'Bot':
            loop.run_until_complete(send(bot, msgs[0].message))
            sleep()
            print('Sending: ' + msgs[0].message)

            bot_msgs = []
            bot_msgs = loop.run_until_complete(receive(bot))
            sleep()
            print('Receiving: ' + bot_msgs[0].message)

            if bot_msgs[0].message:
                loop.run_until_complete(send(myuser, 'Bot: ' + bot_msgs[0].message))

