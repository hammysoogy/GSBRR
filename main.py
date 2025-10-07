import discord
from discord import app_commands
import os

TOKEN = os.getenv("TOKEN")  # your secret bot token (set later in Koyeb)

intents = discord.Intents.default()
bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(bot)

@bot.event
async def on_ready():
    await tree.sync()
    print(f"✅ Logged in as {bot.user}")

@tree.command(name="hello", description="Say hello to the bot")
async def hello_command(interaction: discord.Interaction):
    await interaction.response.send_message(f"👋 Hello, {interaction.user.name}!")

bot.run(TOKEN)
