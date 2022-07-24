import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入') 
    
#導入Discord.py
import discord
#為了asyncio.sleep()
import asyncio
#client是我們與Discord連結的橋樑
client = discord.Client()
    
@client.event
#當有訊息時
async def on_message(message):
    if message.content == '我好帥喔':
        tmpmsg = await message.channel.send('你確定你帥嗎？')
      
# Bot起動
client.run(TOKEN)
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()


