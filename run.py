import discord
import threading
import time
import json

from .clients.CustomClient import CustomClient

with open("secrets.json", "r") as f:
    secrets = json.load(f)

assert "apiKey" in secrets

intents = discord.Intents.default()
intents.members = True

bot = CustomClient(command_prefix="-", intents=intents)

t_run = threading.Thread(target=bot.run, args=(secrets["apiKey"],))
t_run.start()