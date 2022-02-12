from discord.ext import commands
import discord
import random
import threading
import requests
import os
from time import strftime, gmtime, time, sleep
from keep_alive import keep_alive

prefix = '.'
intents = discord.Intents.all()
maincolor = 0x2ecc71
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents, help_command=None)

# config
logschannel = 'Channel ID To Log'


@bot.event
async def on_ready():
  print("Bot Is Ready")

@bot.event
async def on_command_error(ctx, error: Exception):
  if isinstance(error, commands.CommandNotFound):
    return
  else:
    embed = discord.Embed(color=maincolor, description=f'{error}')
    await ctx.send(embed=embed)
  
@bot.command()
async def thelp(ctx):
  embed = discord.Embed(color=0x28dbc9)
  embed.add_field(name="video sharing", value=".tshare (video id) `In Beta Fixing Bugs`")
  embed.add_field(name="video views", value=".tview (video id) `Soon To Come`")
  await ctx.send(embed=embed)

@bot.command()
async def tshare(ctx,vidid):
  embed = discord.Embed(color=0x28dbc9, description=f"sending **10** shares the id **{vidid}**")
  print(f"Send 10 Views To {vidid}")
  await ctx.send(embed=embed)
  logembed = discord.Embed(color=0x2ecc71, description=f"{ctx.author.mention} has sent **300** shares to **{vidid}**")
  await ctx.guild.get_channel(logschannel).send(embed=logembed)
  def bot():
    action_time = round(time())
    device_id = ''.join(random.choice('0123456789') for _ in range(300))
    data = (
        f'action_time={action_time}&item_id={vidid}&item_type=1&share_delta=1&stats_channel=copy'
        )
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-common-params-v2': 'version_code=16.6.5&app_name=musical_ly&channel=App%20Store&devi'
        f'ce_id={device_id}&aid=1233&os_version=13.5.1&device_platform=ip'
        'hone&device_type=iPhone10,5',
        'User-Agent': 'TikTok 16.6.5 rv:166515 (iPhone; iOS 13.6; en_US) Cronet',
        }
    response = requests.post(
                'https://api16-core-c-useast1a.tiktokv.com/aweme/v1/aweme/stats/?ac=WIFI&op_region='
                'SE&app_skin=white&', data=data, headers=headers
    )
    while True:
      threading.Thread(target=bot).start()
      break

keep_alive()

TOKEN = 'discord token here'

bot.run(TOKEN)
