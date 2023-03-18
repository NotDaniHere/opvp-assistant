import discord
from discord.ext import commands
bot = commands.Bot()
print("Insert discord token: ")
token = input()
@bot.slash_command(name="/assist", description="Assists you with things on the sevrer.")
async def first_slash(ctx): 
    await ctx.respond("You executed the slash command!")
    await ctx.respond("")
bot.run(token)
