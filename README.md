# TwitchBot
A simple Twitch bot made in Python

## Installation
* Clone the repository
* Open *cfg.py* and change:
  * `NICK = "Ryibot"` to the name you want the bot to have
  * `CHAN = "ryiseld"` to the name of your Twitch channel
* Create a new file named *oauth.py* that includes the following code:
```python
PASS = "XXX"
```
where XXX is your Twitch chat OAuth password (that you can generate using several sites like [this one](http://www.twitchapps.com/tmi/))
* Open *custom_commands.py*
* Change the conents of the `display_social` function

## How to change or add custom commands
* Open *custom_commands.py*
* Here you can add your own functions, which should probably have a `socket` as a parameter.

## Useful functions
The bot comes with a file named *utils.py* which containts some useful commands for you to use, like `chat` to send a message, `ban` to ban a user, and `is_op` to check if a user is a moderator (useful for commands available to moderators only)
You can obviously add your own functions and do whatever you wish!

To use a command in the `utils.py` file all you have to do is add `import utils` to the beginning of the file (if it's not there already) and use the `utils.` prefix before the function name.