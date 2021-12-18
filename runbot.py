from bot import bot
import json
#import dev

with open("secrets.json", "r") as f:
    secrets = json.load(f)

assert "apikey" in secrets

bot.run(secrets["apikey"])
