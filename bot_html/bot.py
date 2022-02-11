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
flag = 0

@bot.event
async def on_ready():
    global ctx
    channel_id = (config['channel_id'])
    ctx = bot.get_channel(int(channel_id))
    await ctx.send("Broadcasting pool state")
    update.start()
    

@tasks.loop(seconds=20)
async def update():
    list_nodes = []
    global flag
    global ctx
    global old_all_nodes_status
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
            res = [i for i, val in enumerate(all_nodes_status) if not val]
            res2 = [i for i, val in enumerate(old_all_nodes_status) if not val]
            difference = set(res).symmetric_difference(set(res2))
            list_difference = list(difference)
            print(f"list_difference = {list_difference}")
            node_chanches = [list_nodes[i] for i in list_difference] #preparing the list
            print(f"node_chanches = {node_chanches}")
            if flag != 0:
                print(f"flag = {flag}")
                if res != res2:
                    list_difference_boolean = [all_nodes_status[i] for i in list_difference]
                    print(f"list_difference_boolean = {list_difference_boolean}")
                    list_now_healthy_index = [i for i, val in enumerate(list_difference_boolean) if val]
                    list_now_unhealthy_index = [i for i, val in enumerate(list_difference_boolean) if not val]
                    print(f"list_now_healthy_index = {list_now_healthy_index}")
                    print(f"list_now_unhealthy_index = {list_now_unhealthy_index}")
                    if list_now_healthy_index:
                        z = 0
                        list_now_healthy = []
                        for i in list_now_healthy_index:
                            index_for_now_healthy = list_now_healthy_index[z]
                            now_healthy = node_chanches[index_for_now_healthy]
                            print(f"now healthy = {now_healthy}")
                            list_now_healthy.append(now_healthy)
                            z +=1
                        x = 0  
                        for i in list_now_healthy: #send all unhealthy nodes
                            await ctx.send(f"```yaml\n+ {list_now_healthy[x]} is now healthy\n```")
                            x +=1
                            time.sleep(0.5)
                    if list_now_unhealthy_index:
                        z = 0
                        list_now_unhealthy = []
                        for i in list_now_unhealthy_index:
                            index_for_now_unhealthy = list_now_unhealthy_index[z]
                            now_unhealthy = node_chanches[index_for_now_unhealthy]
                            print(f"now unhealthy = {now_unhealthy}")
                            list_now_unhealthy.append(now_unhealthy)
                            z +=1
                        x = 0  
                        for i in list_now_unhealthy: #send all unhealthy nodes
                            await ctx.send(f"```diff\n- {list_now_unhealthy[x]} is now unhealthy\n```")
                            x +=1
                            time.sleep(0.5)
                        
            else:
                x = 0
                for i in node_chanches: #send all unhealthy nodes
                    await ctx.send(f"```diff\n- {node_chanches[x]} is not healthy\n```")
                    x +=1
                    time.sleep(0.5)
        else:
            result = "```yaml\nAll nodes are healthy\n```"
            await ctx.send(result)
            
    old_all_nodes_status = all_nodes_status
    flag = 1

bot.run(TOKEN)