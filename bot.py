import discord
from discord.ext import commands
import schedule_logic

cogs = [schedule_logic]

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())

for index in range(len(cogs)):
  cogs[index].setup(client)

client.run('OTA2NDg2OTMwNjAxMDI5NjUz.YYZVvQ.3mSsoYodZD1ZfbZH9OgekfiU0fc')