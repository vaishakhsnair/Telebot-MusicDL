import os
import time
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterMusic

api_id = 1234 #Here Goes the API ID
api_hash = "asdfghjklxcvbnm124578"  #API HASH

client = TelegramClient("anon", api_id, api_hash)

link = "https://deezer.com/track/1234567"   #A valid deezer or spotify link
path = "dls/"
bot = "FusionDL_Bot"


async def send():
    messages = await client.get_messages(bot, None, reverse=True)
    for i in messages:
        await client.delete_messages(bot, i)
    await client.send_message(bot, link)
    time.sleep(5)


completed = os.listdir(path)
print(completed)
message_list = []


def progress_bar(current, total):
    print((current / total) * 100, "%")


async def dl():
    messages = await client.get_messages(bot, None, reverse=True, filter=InputMessagesFilterMusic)
    message_list.append(messages)
    for i in messages:
        one = i.audio
        name = one.attributes[0].title
        if name + ".flac" not in completed:
            print("Downloading :", name)
            await client.download_media(messages[0], os.path.join(path, name), progress_callback=progress_bar)
            completed.append(name)
        else:
            print(name, ": Already existing")


def change_quality(quality):
    async def ch_qlty(quality):
        await client.send_message(bot, "/settings")
        time.sleep(1)
        async for i in client.iter_messages(bot, reverse=True, from_user=bot):
            message = i
        await message.click(0)
        time.sleep(1)
        async for i in client.iter_messages(bot, reverse=True, from_user=bot):
            message = i
        await message.click(quality)

    with client:
        client.loop.run_until_complete(ch_qlty(quality))


def runner():
    with client:
        client.loop.run_until_complete(send())
        client.loop.run_until_complete(dl())

if __name__ == "__main__":
    runner()
