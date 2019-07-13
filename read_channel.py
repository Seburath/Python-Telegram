from telethon.tl.functions.contacts import ResolveUsernameRequest

client = TelegramClient(session_file, api_id=X, api_hash='X')
client.connect()
response = client.invoke(ResolveUsernameRequest("username"))
print(response.channel_id)
print(response.access_hash)
