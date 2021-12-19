import discord
import re

from discord import user


class CustomClient(discord.Client):
    async def on_ready(self):
        print("------")
        print("DiscordBot: Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

        await self.change_presence(activity=discord.Game(name="being happy ;)"))

    def get_discord_user(self, username, promise):
        members = {}

        for guild in self.guilds:
            for member in guild.members:
                members["#".join([member.name, member.discriminator])] = member.id

        print(members)
        print(promise.resolved)

        if username in members:
            promise.has_joined_discord = True
            promise.discord_id = members[username]
        else:
            promise.has_joined_discord = False
            promise.discord_id = None

        promise.resolve()

    async def send_message(self, id, message):
        userRef = await self.fetch_user(id)

        title = message["title"] + " " + str(userRef)

        embed = discord.Embed(
            title=("".join(re.findall("[^#0-9]", title)) + "!"),
            description=message["description"],
            color=discord.Color.blue(),
        )

        if "subColumns" in message:
            for advice in message["subColumns"]:
                title = advice["title"]
                embed.add_field(name=f"**{title}**", value=advice["description"], inline=False)

        embed.set_footer(text="Made with 💙 by The Statics")

        await userRef.send(embed=embed)
