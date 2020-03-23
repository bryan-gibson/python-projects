# Discord Bot 

import os
#import discord
import random
import pywikibot
from dotenv import load_dotenv
from discord.ext import commands
#from googlesearch import search

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

bot = commands.Bot(command_prefix='!')

site = pywikibot.Site('en', '')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', help='Responds with a random greeting.')
async def greeting(ctx):
    greetings = [
        'Hello!',
        'Hey',
        'How\'s it going?'
    ]
    response = random.choice(greetings)
    await ctx.send(response)

@bot.command(name='roll', help='Simulates D&D related dice rolls.')
async def roll(ctx, dice_load: str, *argv):
    try:
        print (dice_load)
        dice_num = int(dice_load[:dice_load.index('d')])
        dice_sides = int(dice_load[dice_load.index('d') + 1:])
        num_op = -1
        if len(argv) > 0:
            num_op = argv[0]
        print (num_op)
        dice_sum = 0
        dice = [
            str(random.choice(range(1, dice_sides + 1)))
            for x in range(dice_num)
        ]
        for _ in range(len(dice)):
            dice_sum += int(dice[_])
        if num_op != -1:
            num_offset = argv[1]
            if num_op == '+':
                dice_sum += int(num_offset)
            elif num_op == '-':
                dice_sum -= int(num_offset)
            else:
                await ctx.send('Invalid parameter.')
                return False
            await ctx.send("You rolled a **{}** ([{}] {} {})".format(dice_sum,
                ', '.join(dice), num_op, num_offset))
        else:
            await ctx.send("You rolled a **{}** ([{}])".format(dice_sum,
                ', '.join(dice)))
    except:
        await ctx.send('Invalid parameter.')

#@bot.command(name='poe', help='Path of Exile related search.')
#async def poe(ctx, poe_search: str):






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