import discord
import os
import random
from keep_alive import keep_alive
my_secret = os.environ['token']

intents=discord.Intents.default()
intents.members=True
client=discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Da bot is in da server')

@client.event
async def on_message(message):
 if message.content.startswith('$_vc'):
   guild=client.get_guild(742374132133527662)
   channel = client.get_channel({783946002742771753})
   member = client.get_member({820768435557761054})
   await member.move_to(channel)
   await channel.send(f"{member.mention} joined vc")
   await member.edit(voice_channel={channel})
   

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$_hello'):
    await message.channel.send('yo')
  if message.content.startswith('$_Hows the weather?'):
    await message.channel.send('idk, look outside')
  if message.content.startswith('$_I love you'):
    await message.channel.send('kys')
  if message.content.startswith('$_davo'):
    await message.channel.send('GMOs cause autism')
  if message.content.startswith('$_What time is it?'):
    await message.channel.send('idk')
    
@client.event
async def on_member_join(member):
  guild=client.get_guild(742374132133527662)
  channel=guild.get_channel(742374135283580942)
  await channel.send(f"Yo {member.mention}")
  print("Yo")


@client.event
async def on_voice_status_update(member,before,after):
  if before.channel is None and after.channel is not None:
    guild=client.get_guild(742374132133527662)
    channel=guild.get_channel(742374135283580942)
    await channel.send(f"{member.mention} joined vc")
    await member.edit(voice_channel={channel})


keep_alive() 
client.run(my_secret)
