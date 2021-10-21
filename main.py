from telethon import TelegramClient, events,functions
from telethon.tl.types import InputMessagesFilterMusic,Document
import time
import os
api_id = 1234 # here is the api id
api_hash =  "0123456789abcdef0123456789abcdef"   # here is the hash


bot = "FusionDL_Bot"


client = TelegramClient("anon", api_id, api_hash)

link = ""           # a valid deezer music link 

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




