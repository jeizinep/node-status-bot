import asyncio
import platform
import json
import os
import requests
import discord
from discord.ext import commands, tasks

os_type = platform.system()
dir = os.path.dirname(os.path.abspath(__file__)) #finds the directory
if os_type == "Windows":
    raw = open(dir + "\\config.json") #loads the temp.json
    config = json.load(raw)
    raw.close()
if os_type == "Linux":
    raw = open(dir + "/config.json") #loads the temp.json
    config = json.load(raw)
    raw.close()

TOKEN = config['token']

def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    return '%.2f%s' % (num, ['i', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi'][magnitude])

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    name.start()
    activity.start()
    
@tasks.loop(minutes=30)
async def name():
    list_nodes_mainnet = []
    api = config['api_data']
    raw = requests.get(api) #gets the api request
    temp = raw.json()
    for i in temp:
        list_nodes_mainnet.append(i) #loops through the list of nodes and adds them to array
    
    balance_url = "https://" + temp[list_nodes_mainnet[0]]["IotaHornet"]["Domain"] + "/api/v1/addresses/" + config['treasury_address']
    balance_raw = requests.get(balance_url)
    balance_json = balance_raw.json()
    balance = balance_json['data']['balance']
    balance_formatted = f'{human_format(balance)}'
    await bot.user.edit(username=f'Treasury {balance_formatted}')
    
@tasks.loop()
async def activity():
    price_url = config['api_price']
    price_raw = requests.get(price_url)
    price_json = price_raw.json()
    price_usd = round(price_json['market_data']['current_price']['usd'], 3)
    price_eur = round(price_json['market_data']['current_price']['eur'], 3)
    price_chf = round(price_json['market_data']['current_price']['chf'], 3)
    price_change_percent = round(price_json['market_data']['price_change_percentage_24h'], 2)
    if price_change_percent < 0:
        price_change_emoji = "🔻"
    else:
        price_change_emoji = "🔺"
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{price_usd} $ | {price_change_percent}% {price_change_emoji}'))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{price_eur} € | {price_change_percent}% {price_change_emoji}'))
    await asyncio.sleep(10)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f'{price_chf} Fr | {price_change_percent}% {price_change_emoji}'))
    await asyncio.sleep(10)

bot.run(TOKEN)