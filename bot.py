# Discord Bot 

import os
#import discord
import random
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='Hello', help='Responds with a random meme from Marnie & Friends')
async def greeting(ctx):
    meme_quotes = [
        'Wanna play some PoE?!',
        'MICHI!',
        'Do you... Need something?'
    ]

    response = random.choice(meme_quotes)
    await ctx.send(response)

@bot.command(name='roll', help='Simulates dice rolls, idiot.')
async def roll(ctx, dice_load: str):
    num_dice = dice_load[dice_load.index('d')]
    num_sides = dice_load['d':]
    dice = [
        str(random.choice(range(1, num_sides + 1)))
        for x in range(num_dice)
    ]
    await ctx.send(', '.join(dice))

bot.run(TOKEN)



"""
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')



client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds, name=GUILD)

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, I have no idea what Im doing!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    meme_quotes = [
        'Wanna play some PoE?!',
        'MICHI!',
        'Do you... Need something?'
    ]

    if message.content == 'Hello':
        response = random.choice(meme_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

@client.event
async def on_error(event, *args, **kwargs):
    with open('error.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise


#client = CustomClient()
client.run(TOKEN)

"""