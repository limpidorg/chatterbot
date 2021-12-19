import discord


class CustomClient(discord.Client):
    async def on_ready(self):
        print("------")
        print("DiscordBot: Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")

        await self.change_presence(activity=discord.Game(name="conveying happiness ;)"))

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
        await userRef.send(message)
