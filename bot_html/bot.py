import os
import json
import time
import platform
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
old_all_nodes_status = []
old_list_healthy = []
old_list_unhealthy = []
flag = 1

@bot.event
async def on_ready():
    global ctx
    channel_id = (config['channel_id'])
    ctx = bot.get_channel(int(channel_id))
    await ctx.send("Broadcasting pool state")
    update.start()
    

@tasks.loop(seconds=20)
async def update():
    global flag
    global ctx
    global old_all_nodes_status
    global old_list_healthy
    global old_list_unhealthy
    list_nodes = []
    list_healthy = []
    list_unhealthy = []
    raw = open(config['directory_path_html_file']) #loads the temp.json
    temp = json.load(raw)
    raw.close()
    for i in temp:
        list_nodes.append(i) #loops through the list of nodes and adds them to array

    all_nodes_status = []
    y = 0
    for i in temp: #loops through the list of nodes and adds them to array
        shrt = temp[f'{list_nodes[y]}']['dlt.green']['isHealthy']
        all_nodes_status.append(shrt)
        y += 1
    if all_nodes_status != old_all_nodes_status: #
        print(f"all_nodes_status = {all_nodes_status}")
        lie = all(all_nodes_status) # checks if there is a False in the array
        if lie == False: #if there is a False in the array lie = False
            v = 0
            for i in temp: #loops through the list of nodes and adds them to array
                if temp[f'{list_nodes[v]}']['dlt.green']['isHealthy'] is True:
                    shrt_healthy = list_nodes[v]
                    list_healthy.append(shrt_healthy)
                if temp[f'{list_nodes[v]}']['dlt.green']['isHealthy'] is False:
                    shrt_unhealthy = list_nodes[v]
                    list_unhealthy.append(shrt_unhealthy)
                v += 1
            
            difference_healthy = [x for x in list_healthy if x not in old_list_healthy]
            difference_unhealthy = [x for x in list_unhealthy if x not in old_list_unhealthy]
            print(difference_healthy)
            print(difference_unhealthy)
            
            if flag == 0:
                x = 0
                for i in difference_unhealthy: #send all unhealthy nodes
                    await ctx.send(f"```diff\n- {difference_unhealthy[x]} is now unhealthy\n```")
                    x +=1
                    time.sleep(0.5)

                x = 0  
                for i in difference_healthy: #send all healthy nodes
                    await ctx.send(f"```yaml\n+ {difference_healthy[x]} is now healthy\n```")
                    x +=1
                    time.sleep(0.5)
                x = 0
                old_list_healthy = list_healthy
                old_list_unhealthy = list_unhealthy
            else:
                old_list_healthy = list_healthy
                old_list_unhealthy = list_unhealthy
                
        else:
            result = "```yaml\nAll nodes are healthy\n```"
            await ctx.send(result)
      
    old_all_nodes_status = all_nodes_status
    
    print(flag)
    print(list_healthy)
    print(list_unhealthy)
    print(list(old_list_healthy))
    print(list(old_list_unhealthy))
    flag = 0
    
bot.run(TOKEN)