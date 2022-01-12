# 1) Create a discord client class and get "Hello @mention" printed in the chat
import discord
import random
TOKEN = "Insert your token here"
class MyClient(discord.Client):
  pass

# 2) Read !hello command and only then reply with "Hello, @mention"
# 3) Create game instructions response in a separate function
# 4) Build "Rock Paper Scissors" game
# # a) Test if string starts with !play
# # b) Extract user choice by splitting and reading second word (zero based array)
# # c) Make a PC player move using random.option([list of choices])
# # d) Compare if user and PC move are equal. Return "Draw" if they are
# # e) Else:
# # # i)   if user rock then if PC paper I Win else You Win
# # # ii)  if user papper then if PC scissors I Win else You
# # # iii) if user scissors then if PC rock I Win else You

client = MyClient()
client.run(TOKEN)
