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
    
@client.event
#當有訊息時
async def on_message(message):
    if message.content == '碰6要碰啥':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send('肯定卡雷')
        

