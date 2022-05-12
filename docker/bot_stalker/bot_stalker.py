import asyncio
import os
import requests
import discord
from discord.ext import commands, tasks

TOKEN = os.environ.get('TOKEN_STALKER')

bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    name.start()
    activity.start()
    
@tasks.loop(minutes=30)
async def name():
    list_nodes_mainnet = []
    
    api = os.environ.get('API_URL')
    raw = requests.get(api) #gets the api request
    temp = raw.json()
    for i in temp:
        list_nodes_mainnet.append(i) #loops through the list of nodes and adds them to array
    
    balance_url = "https://" + list_nodes_mainnet[0] + "/api/v1/addresses/" + os.environ.get('TREASURY_ADDRESS')
    balance_raw = requests.get(balance_url)
    balance_json = balance_raw.json()
    balance = balance_json['data']['balance']
    if balance > 1000000:
        balance = f'{round(balance / 1000000)} Mi'
    else:
        balance = f'{round(balance / 1000000000)} Gi'
    await bot.user.edit(username=f'Treasury {balance}')
    
@tasks.loop()
async def activity():
    price_url = os.environ.get('PRICE_API')
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