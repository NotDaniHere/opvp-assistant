import discord
import json
from discord.ext import commands
fromjson = ''

#Fully functional including Dockerfile. json doesn't have to be added to requirements as it is default in python.

with open('text.json', "r") as read_file:
    fromjson = (json.load(read_file))
    print(fromjson['mctechnical_details'])
    print(fromjson['play_details'])
    print(fromjson['hardware_details'])
    print(fromjson['twist'])
bot = commands.Bot()
print("Insert discord token, in order to have the bot working with this code: ")
token = input()
@bot.slash_command(description="Technical Server Details")
async def mctechnical_details(ctx): 
    await ctx.respond(fromjson['mctechnical_details'])
@bot.slash_command(description="Enabled options, seed and things that are built on the server.")
async def play_details(ctx): 
    await ctx.respond(fromjson['play_details'])
@bot.slash_command(description="Server hardware info")
async def hardware_details(ctx):
    await ctx.respond(fromjson['hardware_details'])
@bot.slash_command(description="Info about the twist this season.")
async def twist(ctx):
    await ctx.respond(fromjson['twist'])
bot.run(token)