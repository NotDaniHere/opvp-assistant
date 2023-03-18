import discord
from discord.ext import commands
bot = commands.Bot()
print("Insert discord token: ")
token = input()
accepted = 0
rejected = 0
@bot.slash_command(description="Technical Server Details")
async def mctechnical_details(ctx): 
    await ctx.respond("Server details: PaperMC 1.19.3 with QOL vanilla tweaks datapacks. Server IP: mc.optipvp.xyz/optipvp.duckdns.org. Server is running in a Docker Container, and is hosted in Republic of Moldova.")
@bot.slash_command(description="Enabled options, seed and things that are built on the server.")
async def play_details(ctx): 
    await ctx.respond("Currently what we have on the server: Trading Hall, Raid farm, Sugar cane farm, iron farm. Seed is: -1982066951813433173. Nether Hub is a work in progress.")
@bot.slash_command(description="Server hardware info")
async def hardware_details(ctx):
    await ctx.respond("Currently the server is running on 8GB of DDR3 RAM, a 512GB SSD, and an Intel Celeron N2480. About software: Ubuntu 22.04.2 (Pro Activated). And the server is running in a Docker Container (marctv/minecraft-papermc-server).")
@bot.slash_command(description="Vote if the server will reset or if it will not reset.")
async def vote_for_reset(ctx, decision):
    await ctx.respond("Thanks for voting! Your vote may change the future of the server.")
    if decision == "yes":
        print(ctx.author)
        print("has voted Yes!")
    if decision == "no":
        print(ctx.author)
        print("has voted No!")
bot.run(token)