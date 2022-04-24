import os
import json
import time
import platform
import logging
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

bot = commands.Bot(command_prefix='/')
old_all_nodes_status_mainnet = []
old_all_nodes_status_devnet = []
old_list_healthy_mainnet = []
old_list_healthy_devnet = []
old_list_unhealthy_mainnet = []
old_list_unhealthy_devnet = []
flag_mainnet = 1
flag_devnet = 1
logging.basicConfig(filename=config['logfileLocation'], encoding='utf-8', level=logging.DEBUG)

@bot.event
async def on_ready():
    global ctx_mainnet
    global ctx_devnet
    channel_id_mainnet = (config['channel_id_mainnet'])
    channel_id_devnet = (config['channel_id_devnet'])
    ctx_mainnet = bot.get_channel(int(channel_id_mainnet))
    ctx_devnet = bot.get_channel(int(channel_id_devnet))
    await ctx_mainnet.send("Broadcasting pool state")
    await ctx_devnet.send("Broadcasting pool state")
    update.start()
    

@tasks.loop(seconds=20)
async def update():
    global flag_mainnet
    global ctx_mainnet
    global old_all_nodes_status_mainnet
    global old_list_healthy_mainnet
    global old_list_unhealthy_mainnet
    list_nodes_mainnet = []
    list_healthy_mainnet = []
    list_unhealthy_mainnet = []
    raw = open(config['directory_path_html_file']) #loads the temp.json
    temp = json.load(raw)
    raw.close()
    for i in temp:
        list_nodes_mainnet.append(i) #loops through the list of nodes and adds them to array

    all_nodes_status_mainnet = []
    y = 0
    for i in temp: #loops through the list of nodes and adds them to array
        shrt = temp[f'{list_nodes_mainnet[y]}']['dlt.green']['isMainnetHealthy']
        all_nodes_status_mainnet.append(shrt)
        y += 1
    if all_nodes_status_mainnet != old_all_nodes_status_mainnet: #
        logging.debug(f"all_nodes_status = {all_nodes_status_mainnet}")
        lie = all(all_nodes_status_mainnet) # checks if there is a False in the array
        if lie == False: #if there is a False in the array lie = False
            v = 0
            for i in temp: #loops through the list of nodes and adds them to array
                if temp[f'{list_nodes_mainnet[v]}']['dlt.green']['isMainnetHealthy'] is True:
                    shrt_healthy_mainnet = list_nodes_mainnet[v]
                    list_healthy_mainnet.append(shrt_healthy_mainnet)
                if temp[f'{list_nodes_mainnet[v]}']['dlt.green']['isMainnetHealthy'] is False:
                    shrt_unhealthy_mainnet = list_nodes_mainnet[v]
                    list_unhealthy_mainnet.append(shrt_unhealthy_mainnet)
                v += 1
            
            difference_healthy_mainnet = [x for x in list_healthy_mainnet if x not in old_list_healthy_mainnet]
            difference_unhealthy_mainnet = [x for x in list_unhealthy_mainnet if x not in old_list_unhealthy_mainnet]
            logging.debug(difference_healthy_mainnet)
            logging.debug(difference_unhealthy_mainnet)
            
            if flag_mainnet == 0:
                x = 0
                for i in difference_unhealthy_mainnet: #send all unhealthy nodes
                    await ctx_mainnet.send(f"```diff\n- {difference_unhealthy_mainnet[x]} is now unhealthy\n```")
                    x +=1
                    time.sleep(0.5)

                x = 0  
                for i in difference_healthy_mainnet: #send all healthy nodes
                    await ctx_mainnet.send(f"```yaml\n+ {difference_healthy_mainnet[x]} is now healthy\n```")
                    x +=1
                    time.sleep(0.5)
                x = 0
                old_list_healthy_mainnet = list_healthy_mainnet
                old_list_unhealthy_mainnet = list_unhealthy_mainnet
            else:
                old_list_healthy_mainnet = list_healthy_mainnet
                old_list_unhealthy_mainnet = list_unhealthy_mainnet
                
        else:
            await ctx_mainnet.send("```yaml\nAll nodes are healthy\n```")
    
      
    old_all_nodes_status_mainnet = all_nodes_status_mainnet
    
    logging.debug(flag_mainnet)
    logging.debug(list_healthy_mainnet)
    logging.debug(list_unhealthy_mainnet)
    logging.debug(list(old_list_healthy_mainnet))
    logging.debug(list(old_list_unhealthy_mainnet))
    flag_mainnet = 0

    global flag_devnet
    global ctx_devnet
    global old_all_nodes_status_devnet
    global old_list_healthy_devnet
    global old_list_unhealthy_devnet
    list_nodes_devnet = []
    list_healthy_devnet = []
    list_unhealthy_devnet = []
    for i in temp:
        list_nodes_devnet.append(i) #loops through the list of nodes and adds them to array

    all_nodes_status_devnet = []
    y = 0
    for i in temp: #loops through the list of nodes and adds them to array
        shrt = temp[f'{list_nodes_devnet[y]}']['dlt.green']['isDevnetHealthy']
        all_nodes_status_devnet.append(shrt)
        y += 1
    if all_nodes_status_devnet != old_all_nodes_status_devnet: #
        logging.debug(f"all_nodes_status = {all_nodes_status_devnet}")
        lie = all(all_nodes_status_devnet) # checks if there is a False in the array
        if lie == False: #if there is a False in the array lie = False
            v = 0
            for i in temp: #loops through the list of nodes and adds them to array
                if temp[f'{list_nodes_devnet[v]}']['dlt.green']['isDevnetHealthy'] is True:
                    shrt_healthy_devnet = list_nodes_devnet[v]
                    list_healthy_devnet.append(shrt_healthy_devnet)
                if temp[f'{list_nodes_devnet[v]}']['dlt.green']['isDevnetHealthy'] is False:
                    shrt_unhealthy_devnet = list_nodes_devnet[v]
                    list_unhealthy_devnet.append(shrt_unhealthy_devnet)
                v += 1
            
            difference_healthy_devnet = [x for x in list_healthy_devnet if x not in old_list_healthy_devnet]
            difference_unhealthy_devnet = [x for x in list_unhealthy_devnet if x not in old_list_unhealthy_devnet]
            logging.debug(difference_healthy_devnet)
            logging.debug(difference_unhealthy_devnet)
            
            if flag_devnet == 0:
                x = 0
                for i in difference_unhealthy_devnet: #send all unhealthy nodes
                    await ctx_devnet.send(f"```diff\n- {difference_unhealthy_devnet[x]} is now unhealthy\n```")
                    x +=1
                    time.sleep(0.5)

                x = 0  
                for i in difference_healthy_devnet: #send all healthy nodes
                    await ctx_devnet.send(f"```yaml\n+ {difference_healthy_devnet[x]} is now healthy\n```")
                    x +=1
                    time.sleep(0.5)
                x = 0
                old_list_healthy_devnet = list_healthy_devnet
                old_list_unhealthy_devnet = list_unhealthy_devnet
            else:
                old_list_healthy_devnet = list_healthy_devnet
                old_list_unhealthy_devnet = list_unhealthy_devnet
                
        else:
            await ctx_devnet.send("```yaml\nAll nodes are healthy\n```")
    
      
    old_all_nodes_status_devnet = all_nodes_status_devnet
    
    logging.debug(flag_devnet)
    logging.debug(list_healthy_devnet)
    logging.debug(list_unhealthy_devnet)
    logging.debug(list(old_list_healthy_devnet))
    logging.debug(list(old_list_unhealthy_devnet))
    flag_devnet = 0

bot.run(TOKEN)