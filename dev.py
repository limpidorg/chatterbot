import discord
from bot import bot, dispatchSendMessageEvent

testUser = "yyjlincoln#5912"


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