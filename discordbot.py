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

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if client.user in message.mentions: # @判定
        translator = googletrans.Translator()
        robotName = client.user.name
        first, space, content = message.clean_content.partition('@'+robotName+' ')
        
        if content == '':
            content = first
        if translator.detect(content).lang == DSTLanguage:
            return
        if translator.detect(content).lang == SRCLanguage or SRCLanguage == '':
            remessage = translator.translate(content, dest='zh-tw').text
            await message.reply(remessage) 

# Bot起動
client.run(TOKEN)
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()

@client.event
#當有訊息時
async def on_message(message):
    if message.content == '碰6要碰啥':
        #刪除傳送者的訊息
        await message.delete()
        #然後回傳訊息
        await message.channel.send('肯定卡雷')
        
client.run('OTk4ODMwNDM3NDQwOTU0NDM5.Goq4AK.1AyF2jZ8CQ5y1dpLoBeyanb6CeZzbyckW63I04')
