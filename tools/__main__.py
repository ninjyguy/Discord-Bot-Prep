import discord
TOKEN = "<Add token string here>"

claimed_rooms = {}

class DiscordDriverClient(discord.Client):
  async def on_ready(self):
    print("Connection is ready")

  async def on_group_join(self, channel, user):
    print("User joined the group")
    print(channel.__dict__)
    print(user.__dict__)

  async def on_message(self, message):
    if message.author.id == self.user.id:
        return
    print("==========================")
    print("Message received")
    print(message.channel)
    print(message.author)
    print(message.content.lower())
    if message.channel.name == "testing":
      if message.content.lower().strip() == "!claim":
        print("Responding")
        await message.channel.send(f"Hey there {message.author.name}!!! Let's find you a private room!!!")
        # print(message.guild.roles)
        role = await self._add_role(message)
        if role is not None:
          await message.channel.send(f"{message.author.name} => bot-{role.name[4:]} channel is yours...")
      if message.content.lower().strip().startswith("!clear"):
        await message.channel.send("Clearing roles...")
        await self._remove_role(message)
      if message.content.lower().strip().startswith("!list"):
        await self._list_claims(message)
        
        
  async def _list_claims(self, message):
    response = "Listing Roles:\n"
    # members = await message.guild.fetch_members()
    for member in message.mentions:
      roles = [r.name for r in member.roles if r.name.startswith( "Dev")]
      response += f"{member.name} => {','.join(roles)}\n"
    await message.channel.send(response)

  async def _add_role(self, message):
    existing_dev_roles = [r for r in message.author.roles if r.name.startswith("Dev")]
    if existing_dev_roles:
      await message.channel.send(f"You already have room bot-{existing_dev_roles[0].name[4:]} assigned to you.")
      return None
    guild_roles = await message.guild.fetch_roles()
    print("Guild Roles")
    print(guild_roles)
    print({r.name:r.members for r in guild_roles if r.name.startswith( "Dev")})
    role = [r for r in guild_roles if r.name.startswith( "Dev") and r.name not in claimed_rooms][0]
    print(role)
    print(message.author.roles)
    await message.author.add_roles(role)
    claimed_rooms[role.name] = message.author.name
    print(claimed_rooms)
    return role

  async def _remove_role(self, message):
    if(message.author.name not in ["Patrice", "spunchbop","deanForward"]):
      await message.channel.send("Error: No permitted to execute command!!!")
      return;
    print("Mentions %s", message.mentions)
    for member in message.mentions:
      remove_roles = [r for r in member.roles if r.name.startswith("Dev")]
      print(remove_roles)
      for r in remove_roles:
        await member.remove_roles(r)
        if r.name in claimed_rooms:
          del claimed_rooms[r.name]

client = DiscordDriverClient()
client.run(TOKEN)
