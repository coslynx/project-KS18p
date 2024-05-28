# main.py (Python)

import discord
from discord.ext import commands
import bot
import commands
import auto_moderation
import logging_system
import user_interface
import custom_rules
import update_system

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

# Add commands from commands.py
bot.add_cog(commands.Commands(bot))

# Add auto-moderation features
auto_moderation.setup(bot)

# Add logging system
logging_system.setup(bot)

# Add user interface
user_interface.setup(bot)

# Add custom rules setup
custom_rules.setup(bot)

# Add update system
update_system.setup(bot)

# Run the bot
bot.run('your_token_here')