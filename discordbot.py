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
import random
async def on_message(message):
    if message.content == '111':
       names = ['John', 'Juan', 'Jane', 'Jack', 'Jill', 'Jean']
       def selectRandom(names):
       return random.choice(names)

print("The name selected is: ", selectRandom(names))
                
# Bot起動
client.run(TOKEN)
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()




