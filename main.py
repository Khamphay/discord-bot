import discord
from discord.ext import commands


bot = commands.Bot(
    command_prefix="!",
    intents=discord.Intents.all()
)

token = "your token"
ch1 = "your channel id" # ID Channel must be integer

@bot.event
async def on_ready():
    print(f"บอทออนแล้วไอสัส {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(ch1)
    text = f"**# ยินต้อนรับ เข้า เซิฟครับ {member.mention}!**"
    await channel.send(text)

bot.run(token)
