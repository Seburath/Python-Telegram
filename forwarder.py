import asyncio
from time import sleep
from collections import defaultdict

from telethon import TelegramClient


class AutoForwarder:
    def __init__(self, user):
        session = 'session2'
        api_id = 
        api_hash = ''
        phone = ''

        self.name = user
        self.client = TelegramClient(session , api_id, api_hash).start(phone)
        self.client.start()
        self.loop = asyncio.get_event_loop()
        self.msgs = defaultdict()
        self.last_msg = ''

    async def async_receive(self, user):
        msgs = []
        async for msg in self.client.iter_messages(user, limit=2):
            msgs.append(msg)

        return msgs

    async def async_send(self, user, msg):
        await self.client.send_message(user, msg)

    def receive(self, user):
        msgs = self.loop.run_until_complete(self.async_receive(user))
        self.msgs[user] = [msgs[0].message, msgs[1].message]

    def send(self, user, msg):
        self.loop.run_until_complete(self.async_send(user, msg))

    def have_new_msg(self):
        self.receive(self.name)
        msg = self.msgs[self.name][0]

        if msg != self.last_msg:
            self.last_msg = msg
            return True
        else:
            return False

    def get_msgs_from(self, user):
        self.receive(user)
        return self.msgs[user]

    def get_last_msg(self):
        msg = self.get_msgs_from(self.name)[0]
        return msg

    def send_last_msg_to(self, user):
        msg = self.get_last_msg()
        self.send(user, msg)

    def send_previous_msg_to(self, user):
        msg = self.get_msgs_from(self.name)[1]
        self.send(user, msg)

    def autosend_last_msg_from(self, user):
        self.get_msgs_from(user)
        self.send(self.name, 'bot: ' + self.msgs[user][0])


if __name__ == '__main__':
    user = AutoForwarder('seburath')
    translator = 'YTranslateBot'
    bot = 'Quickchat_Emerson_bot'

    while True:
        sleep(0.1)
        if user.have_new_msg():
            msg = user.get_last_msg()
            if msg == 'Translate' :
                user.send_previous_msg_to(translator)
                sleep(1)
                user.autosend_last_msg_from(translator)
            elif msg.split(':')[0] in ['bot', 'Español']:
                pass
            else:
                user.send_last_msg_to(bot)
                sleep(1)
                user.autosend_last_msg_from(bot)
