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
![Alt text](images\Applications.png?raw=true "Title")

You'l need to install python3 and pip
```shell
sudo apt-get update
sudo apt-get install python
sudo apt install python3-pip
```

then you can install the python libraries
```shell
cd ~/node-status-bot
sudo pip install requirements.txt
```

then chose the method of getting the pool state (api is recommended)
```shell
cd /bot_api
```

modify the config to your liking ("token" is your bots api token, "channel_id" is your desired channel id, "api" is the api url from which you get your pool state [recommended is dlt.greens pool mana](https://dlt.green/dns/dltgreen_poolmana))
```shell
nano config.json
```

now you are ready to start the skript
```shell
python3 bot.py
```

## Author

👤 **Snowli**

* Twitter: [@Snowli111](https://twitter.com/Snowli111)
* Github: [@Snowli11](https://github.com/Snowli11)

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2022 [Snowli](https://github.com/Snowli11).<br />
This project is [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html) licensed.
