import discord
from discord.ext import commands
from discord import app_commands
import os
import config

# intents setup
intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(command_prefix="/", intents=intents)

# Put bot online
bot.run(config.DCBOTTOKEN)