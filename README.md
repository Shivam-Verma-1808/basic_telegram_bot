
# Basic Telegram Bot

A basic python telegram bot.



## Demo

<img src="./demo/demo_gif" />

![Telegram app bot demo](./demo/demo_gif)
![PC Screenshot](./demo/Screenshot)


![Telegram app bot demo](https://drive.google.com/file/d/1FW2a2y3mxitRlMRZlVMh5_puVy6j0c2C/view?usp=drive_link)
![PC Screenshot](https://drive.google.com/file/d/1U6coFc4YzT-nLELRpd9O0UKSqJk5uLi6/view?usp=drive_link)


## Documentation
* Telegram->BotFather->Create new bot
     (reference [create_new_bot](https://core.telegram.org/bots/features#creating-a-new-bot)) 
* make a new python virtual environment
```
    $python -m venv telegram_bot_env
```
* activate the "telegram_bot_env" python virtual environment
```
    $.\telegram_bot_env\Scripts\activate
```
* goto your project
```
    $cd  <project path>
```
* crate a .env file (lets say "telegram_bot_tokken_keys.env") to store your bot's token
```
    $pip install python-dotenv <-------for managing telegram bot token
```
* copy the generated bot token to .env
* add .env file to .gitignore
```
    .gitignore <------------for ignoring .env 
```
* install python pkg "python-telegram-bot" to communicate with telegram
```
    $pip install python-telegram-bot==20.7
    $python.exe -m pip install --upgrade pip
    $pip show python-telegram-bot
        Name: python-telegram-bot
        Version: 20.7
        Summary: We have made you a wrapper you can't refuse
        Home-page: https://python-telegram-bot.org/
        Author: Leandro Toledo
        Author-email: devs@python-telegram-bot.org
        License: LGPLv3
        Location: C:\Users\shiva\telegram_bot_env\Lib\site-packages
        Requires: httpx
        Required-by:
```
* execute
```
    $python ./telegram_bot.py
```
