import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']


client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入') 
    
# 收到訊息時呼叫
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    #如果包含 ping，機器人回傳 pong
    if message.content == '殺人魔':
        await message.channel.send('噁心')


# Bot起動
client.run(TOKEN)
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()


# Bot起動
client.run(TOKEN)
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()


