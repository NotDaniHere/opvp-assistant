import discord
import json
from discord.ext import commands
fromjson = ''


with open('text.json', "r") as read_file:
    fromjson = (json.load(read_file))
bot = commands.Bot()
print("Insert discord token: ")
token = input()
@bot.slash_command(description="Technical Server Details")
async def mctechnical_details(ctx): 
    await ctx.respond(fromjson[mctechnical_details])
@bot.slash_command(description="Enabled options, seed and things that are built on the server.")
async def play_details(ctx): 
    await ctx.respond(fromjson[play_details])
@bot.slash_command(description="Server hardware info")
async def hardware_details(ctx):
    await ctx.respond(fromjson[hardware_details])
bot.run(token)