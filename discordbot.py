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
    
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()

@client.event
#當有訊息時
async def on_message(message):
    if message.content == '酷':
        #然後回傳訊息
        await message.channel.send('酷的')
        
@client.event
#當有訊息時
async def on_message(message):
    if message.content == '碰6要碰啥':
        #然後回傳訊息
        await message.channel.send('肯定卡雷')
        
@client.event
#當有訊息時
async def on_message(message):
    if message.content == '我好帥喔':
        #然後回傳訊息
        await message.channel.send('你長得跟屎一樣')
                
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


