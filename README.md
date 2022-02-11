<h1 align="center">Welcome to dlt.green node-status-bot 👋</h1>
<p>
  <img alt="Version" src="https://img.shields.io/badge/version-1.0.0-blue.svg?cacheSeconds=2592000" />
  <a href="https://www.gnu.org/licenses/gpl-3.0.html" target="_blank">
    <img alt="License: GNU General Public License v3.0" src="https://img.shields.io/badge/License-GNU General Public License v3.0-yellow.svg" />
  </a>
  <a href="https://twitter.com/Snowli111" target="_blank">
    <img alt="Twitter: Snowli111" src="https://img.shields.io/twitter/follow/Snowli111.svg?style=social" />
  </a>
</p>

> Use this bot to keep your discord up to date on the dlt.green node-pool status

### 🏠 [Homepage](https://dlt.green)

## Getting started

First you need to create a new Discord bot on [the official website](https://discord.com/developers/applications)
![Create application](https://github.com/Snowli11/node-status-bot/blob/main/images/Applications.png?raw=true)

Go to bot


![Choose bot](https://github.com/Snowli11/node-status-bot/blob/main/images/Choose%20Bot.png?raw=true)

Add bot
![Add bot](https://github.com/Snowli11/node-status-bot/blob/main/images/Add%20bot.png?raw=true)

Go to URL Generator
![Url generator](https://github.com/Snowli11/node-status-bot/blob/main/images/URL%20Generator.png?raw=true)

Create bot url
![bot url](https://github.com/Snowli11/node-status-bot/blob/main/images/Create%20bot%20url.png?raw=true)

Open generated link and invite bot to your discord



![invite bot](https://github.com/Snowli11/node-status-bot/blob/main/images/Select%20server.png?raw=true)

Go back to bot


![Choose bot](https://github.com/Snowli11/node-status-bot/blob/main/images/Choose%20Bot.png?raw=true)

Copy bot token


![Bot token](https://github.com/Snowli11/node-status-bot/blob/main/images/Copy%20token.png?raw=true)


# Linux

You need to install python3 and pip if it isn't installed already
```shell
sudo apt-get update
sudo apt-get install python
sudo apt install python3-pip
```

now download the newest release and unzip the code

then chose the method of getting the pool state (api is recommended)
```shell
cd /bot_api
```

then you can install the python libraries
```shell
cd ~/node-status-bot
sudo pip install requirements.txt
```

modify the config to your liking ("token" is your bots api token, "channel_id" is your desired channel id, "api" is the api url from which you get your pool state [recommended is dlt.greens pool mana](https://dlt.green/dns/dltgreen_poolmana))
```shell
nano config.json
```

now you are ready to start the skript
```shell
python3 bot.py
```

# Windows

Download the latest python version form the [windows store](https://www.microsoft.com/store/productId/9PJPW5LDXLZ5) or the [python website](https://www.python.org/downloads/) (Website is recommended)

now download the newest release and unzip the code

then chose the method of getting the pool state (api is recommended)
```shell
cd bot_api
```
install the requirements
```shell
pip install requirements.txt
```

open the config.json with your text editor of choice and edit the config.json to your liking.
("token" is your bots api token, "channel_id" is your desired channel id, "api" is the api url from which you get your pool state [recommended is dlt.greens pool mana](https://dlt.green/dns/dltgreen_poolmana))

now you are ready to start the skript
```shell
python3 bot.py
```

## Author

👤 **Snowli**

* Twitter: [@Snowli111](https://twitter.com/Snowli111)
* Github: [@Snowli11](https://github.com/Snowli11)
* Discord: Snowli#2806

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2022 [Snowli](https://github.com/Snowli11).<br />
This project is [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) licensed.
