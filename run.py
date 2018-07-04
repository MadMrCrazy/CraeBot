print("Running discord bot")
token = "token input"
import config
if config.token == "":
    print("Initialisation error, Insert bot token in config.py")
else:
    print("Config Imported!")
    import main
    bot = main.crae
    bot.run(config.token)
