import asyncio
import discord
import threading
import time
import json
import asyncio

from .clients.CustomClient import CustomClient

with open("secrets.json", "r") as f:
    secrets = json.load(f)

assert "apiKey" in secrets

intents = discord.Intents.default()
intents.members = True

bot = CustomClient(command_prefix="-", intents=intents)

loop = asyncio.get_event_loop()
loop.create_task(bot.start(secrets["apiKey"]))
t_run = threading.Thread(target=loop.run_forever)
t_run.start()
