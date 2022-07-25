import discord
import googletrans
import os
import random
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
        
# 收到訊息時呼叫
@client.event
async def on_message(message):
    
    # 送信者為Bot時無視
    if message.author.bot:
        return
    await client.process_commands(message)
    #私訊
    if message.guild == None:
        return
    result = service.spreadsheets().values().get(
    spreadsheetId=SpreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    if not values:
        return
    else:
        for row in values:
            if (message.channel.name == row[0] or row[0] == ''):
                keywords = row[1].split()
                check = True
                for keyword in keywords:
                    if not keyword in message.content:
                        check = False
                        break
                if check:
                    if message.author.nick == None:
                        username = message.author.name
                    else:
                            username = message.author.nick
                    if '<ban>' in row[2]:
                        await message.author.ban()
                    else:
                        if '<kick>' in row[2]:
                            await message.author.kick()
                        if '<delete>' in row[2]:
                            await message.delete()
                        else:
                            if '<reply>' in row[2]:
                                await message.reply(row[3].replace('<username>',username))
                            if '<replyrandom>' in row[2]:
                                msgs = row[3].split('|')
                                if len(msgs) != 0:
                                    index = random.randint(0, len(msgs)-1)
                                    await message.reply(msgs[index].replace('<username>',username))
                    if '<send>' in row[2]:
                        await message.channel.send(row[3].replace('<username>',username))
                    if '<sendrandom>' in row[2]:
                        msgs = row[3].split('|')
                        if len(msgs) != 0:
                            index = random.randint(0, len(msgs)-1)
                            await message.channel.send(msgs[index].replace('<username>',username))
                    return
                
# Bot起動
client.run(TOKEN)
#導入Discord.py
import discord
import time
#client是我們與Discord連結的橋樑
client = discord.Client()




