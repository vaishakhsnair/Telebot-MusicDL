from telethon import TelegramClient, events,functions
from telethon.tl.types import InputMessagesFilterMusic
import time
from telethon.tl.types import Document
import os
api_id = 8828647
api_hash = "61b3bd6272e586d5bd214ffb822321f4"


bot = "FusionDL_Bot"


client = TelegramClient("anon", api_id, api_hash)

link = "https://deezer.com/track/1398346782"

path = "dls/"
async def send():

    message = await client.send_message(bot, link)
    time.sleep(5)

completed = os.listdir(path)
message_list = []

async def dl():
    messages = await client.get_messages(bot,None, reverse=True,filter = InputMessagesFilterMusic)
    print(len(messages))
    message_list.append(messages)
    for i in messages:
        one = i.audio
        name = one.attributes[0].title
        print(name)
        if name+".flac" not in completed:
            print("Downloading :",name)
            await client.download_media(messages[0],path+name)
            completed.append(name)
        else:
            print(name,": Already existing")

   


    
def runner():
    with client:
        client.loop.run_until_complete(send())
        client.loop.run_until_complete(dl())
    

if __name__ == "__main__":
    runner()




