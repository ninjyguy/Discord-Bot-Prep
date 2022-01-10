# Creating A Bot
## Import libraries we need and store token in a variable
```python
import discord
import random
TOKEN = "Insert your token here"

```
## Create My client class and launch it
```python
import discord
import random
TOKEN = "Insert your token here"

# make my client exactly as discord client
class MyClient(discord.Client):
    pass

# create one copy of it
client = MyClient()
# start that copy with a token and let it run for ever
client.run(TOKEN)
```
## Make sure the bot doesn't reply to itself
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return




client = MyClient()
client.run(TOKEN)
```
## Get "Hello @mention" printed in the chat on command: !hello
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            message.channel.send(f"Hello, {message.author.name}")




client = MyClient()
client.run(TOKEN)
```
#  Build "Rock Paper Scissors" game
##  Create game instructions response in a separate function
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")




client = MyClient()
client.run(TOKEN)
```
##  Test if string starts with !play
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)
        await self.play(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            




client = MyClient()
client.run(TOKEN)
```
##  Extract user choice by splitting and reading second word (zero based array)
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            #get user move
            user_move = message.content.split(' ')[1]




client = MyClient()
client.run(TOKEN)
```
##  Make a PC player move using random.option([list of choices])and print it
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            #get user move
            user_move = message.content.split(' ')[1]
            #make move
            pc_move = random.choice(["rock", "paper", "scissors"])
            print(pc_move)




client = MyClient
client.run(TOKEN)
```
##  Compare if user and PC move are equal. Return "Draw" if they are
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            #get user move
            user_move = message.content.split(' ')[1]
            #make move
            pc_move = random.choice(["rock", "paper", "scissors"])
            print(pc_move)
            #compare moves and announce winner
            if user_move == pc_move:
                await message.channel.send("Draw!")




client = MyClient()
client.run(TOKEN)
```
## Else:
### if user_move = rock and if PC_move  = scissors: You win  else: I Win
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            #get user move
            user_move = message.content.split(' ')[1]
            #make move
            pc_move = random.choice(["rock", "paper", "scissors"])
            print(pc_move)
            #compare moves and announce winner
            if user_move == pc_move:
                await message.channel.send("Draw!")
            else:
                if user_move == "rock":
                    if pc_move == "scissors":
                        await message.channel.send("You win!")
                    else:
                        await message.channel.send("I win!")




client = MyClient()
client.run(TOKEN)
```
### if user_move = paper and if PC_move = rock: You Win else: I win

```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)
        await self.play(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            #get user move
            user_move = message.content.split(' ')[1]
            #make move
            pc_move = random.choice(["rock", "paper", "scissors"])
            #compare moves and announce winner
            if user_move == pc_move:
                await message.channel.send("Draw!")
            else:
                if user_move == "rock":
                    if pc_move == "scissors":
                        await message.channel.send("You win!")
                    else:
                        await message.channel.send("I win!")
                elif user_move == "paper":
                    if pc_move == "rock":
                        await message.channel.send("You win!")
                    else:
                        await message.channel.send("I win!")




client = MyClient()
client.run(TOKEN)
```
### if user_move = scissors and if PC_move = paper: You Win else: I win
```python
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        
        if message.content.startswith("!hello"):
            await message.channel.send(f"Hello, {message.author.name}")
        
        await self.help(message)
        await self.play(message)

    async def help(self, message):
        if message.content.startswith("!help"):
            await message.channel.send("Your bot description goes here")

    async def play(self, message):
        if message.content.startswith("!play"):
            #get user move
            user_move = message.content.split(' ')[1]
            #make move
            pc_move = random.choice(["rock", "paper", "scissors"])
            #compare moves and announce winner
            if user_move == pc_move:
                await message.channel.send("Draw!")
            else:
                if user_move == "rock":
                    if pc_move == "scissors":
                        await message.channel.send("You win!")
                    else:
                        await message.channel.send("I win!")
                elif user_move == "paper":
                    if pc_move == "rock":
                        await message.channel.send("You win!")
                    else:
                        await message.channel.send("I win!")
                else: #user_move == "scissors"
                    if pc_move == "paper":
                        await message.channel.send("You win!")
                    else:
                        await message.channel.send("I win!")




client = MyClient()
client.run(TOKEN)
```
