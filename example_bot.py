import discord
import discord
from discord.ext import commands
from random import random
import time
import json

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
bot = commands.Bot(command_prefix = '*', intents = intents)


@bot.event
async def on_ready():
    print("Bot is ready")

@bot.event
async def on_member_join(member):
    print(f"{member} がきました.")

@bot.event
async def on_member_remove(member):
    print(f"{member} が行きました.")

@bot.command()
async def hello(ctx):
    await ctx.send("こんにちわ！")
'''
@bot.command(aliases=['D', 'Dice', 'Roll'])
async def r1(ctx, * , num):
    await ctx.send(f"Rolling a D{num}!")
    await ctx.send(int(random()*int(num)) + 1)
'''
@bot.command(aliases=['D','Dice', 'Roll'])
async def rx(ctx, num, times = 1):
    i = 0
    times = int(times)
    total = 0
    string = ""
    await ctx.send(f"Rolling a D{num} {times} times!")
    for i in range(times):
        inst = int(random()*int(num)) + 1
        string += (str(inst) + "  ")
        total += inst
    await ctx.send(f"Sequence: {string}")
    await ctx.send(f"Total: {total}!")
    time.sleep(5)
    await ctx.channel.purge(limit = 4)

up_messagelist = ["sign up", "Sign Up", "SignUp", "signup", "su"]
down_messagelist = ["drop out", "Drop Out", "DropOut", "dropout", "do"]
@bot.event
async def on_message(message):
    print("______________________________________")
    user = str(message.author.id)
    author = str(message.author)
    List = ''
    if "@!7904125296367370" in message.content:
        string = message.content[23:]
        print("Message: " + string)
        if string in up_messagelist:
            print("Found sign up request")
            with open("signup.json", 'r') as f:
                List = json.load(f)
                if user in List:
                    print("Already in json")
                else:
                    List[user] = author
                    print("Added to json")
                    
            with open("signup.json", 'w') as f:
                json.dump(List, f, indent=4)

        elif string in down_messagelist:
            print("Found quit request")
            with open("signup.json", 'r') as f:
                List = json.load(f)
                if user not in List:
                    print("Not found in json")
                else:
                    del List[user]
                    print("Deleted from json")

            with open("signup.json", 'w') as f:
                json.dump(List, f, indent=4)

        await message.add_reaction('\U0001F44D')
        
    
bot.run(#token goes here)