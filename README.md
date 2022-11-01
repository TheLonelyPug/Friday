# Flat Fuck Friday

| Requirements | Links |
| ------ | ------ |
| Discord.py 1.7.0 | [https://pypi.org/project/discord.py/1.7.0/] |
| bot.py | [https://github.com/TheLonelyPug/Friday/blob/main/bot.py] |
| .env | [Generate your own]
| catfriday.mp4 | [https://github.com/TheLonelyPug/Friday/blob/dev/catfriday.mp4] |
| alligatorfriday.mp4 | [https://github.com/TheLonelyPug/Friday/blob/dev/alligatorfriday.mp4]



## setup and installation

Discord Developer Portal

```sh
Set up application on https://discord.com/developers/applications/

Go to OAuth2, click bot.

Give bot Send messages Manage messages in text permissions.

Copy the url that is generated and invite your bot
```

bot.py and .env setup

```sh
$ Make a folder for the bot
$ Copy bot.py and friday.mp4 to the folder
$ Create a .env file and put <token = your_token> without the <> in that file
$ Add Your channel ID after ID = 
$ Run the bot with 'python bot.py'
```` 


Discord.py 1.7.0

```sh
$ pip install discord.py==1.7.0 or py -3 -m pip install -U discord.py==1.7.0 or if the previous doesn't work
```

FFMPEG-Static

```sh
$ npm install ffmpeg-static
```

## Running the bot

```sh
$ python.exe bot.py or python bot.py
```


## Usage

```sh
The bot send scheduled messages using aiocron.
You can change the current cronjob that has been set to anything using https://crontab.guru/
```
