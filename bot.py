from discord.ext import commands, tasks
from discord.utils import get
import discord

import re

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(intents=intents, command_prefix="!")

testUser = "yyjlincoln#5912"
# testUser = "Bonsaï#8521"


@bot.event
async def on_ready():
    print("------")
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("------")

    dispatchSendMessageEvent(
        testUser,
        {
            "title": f"Hello {testUser}",
            "description": "Here is the reason of my message.",
            "advices": [
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
                {
                    "title": "Don't be rude!",
                    "description": "The person you are talking to might be going through hard times...",
                },
            ],
        },
    )

    await bot.change_presence(activity=discord.Game(name="conveying happiness ;)"))


@bot.event
async def on_send_message(username, message):
    members = {}

    for guild in bot.guilds:
        for member in guild.members:
            members["#".join([member.name, member.discriminator])] = member.id

    if username in members:
        userRef = await bot.fetch_user(members[username])

        embed = discord.Embed(
            title="".join(re.findall("\D[^#0-9]", message["title"])),
            description=message["description"],
            color=discord.Color.blue(),
        )

        for advice in message["advices"]:
            title = advice["title"]
            embed.add_field(name=f"**{title}**", value=advice["description"], inline=True)

        embed.set_footer(text="Made with 💙 by The Statics")

        await userRef.send(embed=embed)
    else:
        print("User not found!")


def dispatchSendMessageEvent(username, message):
    bot.dispatch("send_message", username, message)


bot.run("OTIxNjgxOTg0MDM0NTk4OTIz.Yb2dPQ.xb1BnBZ5TkmOkJyT40qGtXmN-dk")
