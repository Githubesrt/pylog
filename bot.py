import discord
from discord.ext import commands
import os
import requests

# --- CONFIG ---
TOKEN = 'YOUR_BOT_TOKEN'
MY_ID = 123456789012345678  # Your Discord User ID
VERCEL_URL = "https://your-project.vercel.app"

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# --- ACCOUNT GENERATION LOGIC ---
def create_account():
    # Insert your Puppeteer/Selenium or Request logic here
    # For now, it's a placeholder
    return "User_Omer:Pass12345"

@bot.event
async def on_ready():
    print(f'📡 UAE Node Online: Logged in as {bot.user}')

@bot.command()
async def setup(ctx):
    if not ctx.message.attachments:
        return await ctx.send("Please upload an image with the command.")

    # Get the image link from Discord
    attachment = ctx.message.attachments[0]
    img_url = attachment.url

    # Create the clickable Markdown link
    # When clicked, it takes you to the Vercel trigger
    trigger_link = f"{VERCEL_URL}/api/create?user={ctx.author.name}"
    clickable_image = f"[![SYSTEM]({img_url})]({trigger_link})"

    await ctx.send(clickable_image)
    await ctx.message.delete()

@bot.event
async def on_message(message):
    # This listens for the "!trigger_ai" command sent by your Vercel Webhook
    if message.content.startswith('!trigger_ai'):
        target_user = message.content.split(' ')[1]
        
        # 1. Generate the account
        account_data = create_account()
        
        # 2. DM the results to you
        user = await bot.fetch_user(MY_ID)
        embed = discord.Embed(title="🔓 ACCOUNT GENERATED", color=0x00ff00)
        embed.add_field(name="Target", value=target_user)
        embed.add_field(name="Credentials", value=f"`{account_data}`")
        
        await user.send(embed=embed)

    await bot.process_commands(message)

bot.run(TOKEN)
