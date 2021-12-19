import discord


class CustomClient(discord.Client):
    async def on_ready(self):
        print("------")
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

        await self.change_presence(activity=discord.Game(name="conveying happiness ;)"))

    def has_joined_discord(self, username, event):
        members = {}

        for guild in self.guilds:
            for member in guild.members:
                members["#".join([member.name, member.discriminator])] = member.id

        print(members)

        if username in members:
            event.has_joined_discord = members[username]
        else:
            event.has_joined_discord = False

    async def send_message(self, id, message):
        userRef = await self.fetch_user(id)
        await userRef.send(message)
