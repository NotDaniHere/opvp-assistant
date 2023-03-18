import discord
import time
from discord.ext import commands
mainClient = commands.Bot(command_prefix="/", intents =discord.Intents.all())
print("Insert discord token: ")
mainToken = input()
intents = discord.Intents.default()
intents.message_content = True
@mainClient.command()
async def assist(ctx, member:discord.Member = None):
    if member == None:
        member == ctx.author
    embed = discord.Embed(title="Server Assistance!", description="Auto-assists you with everything you may need on the server.", colour=discord.Colour.random())
    embed.add_field(name="Minecraft Server Details", value = "Seed is: -1982066951813433173; Server Version is 1.19.3; The Server is running on PaperMC, with a bunch of VanillaTweaks QOL improving datapacks.") 
    embed.add_field(name="Why am I experiencing so much ping lag?", value="You may experience it because the server is hosted in Moldova (Eastern Europe) so that answers why you have such ping. To make it better please connect to the internet using ethernet, thanks:)")
    embed.add_field(name="Why is the server so laggy (not ping related)?", value="The server may lag a lot when generating a lot of chunks, and that is normal, since the server is basically a really weak laptop processor with 8gb of ram(plenty) and an ssd. The bottleneck here is the CPU. Why can't it be better? Since it uses a low amount of power, but upgrading to something faster may be noisy and non-powerefficient, so we are stuck with this server for now until I can get a better one up and running some day.")
    embed.add_field(name="When will the server end?",value="The server will end when all of us are bored of Minecraft and/or want a reset since the world has become repetitive/old/laggy. But I think I can guarantee that thorugh 2023 it will stay up mostly 24/7 while I can maintain it.")
    embed.add_field(name="Bare Metal Details", value = "CPU: Intel Celeron N2480 2 core 2 thread 2.54Ghz Turbo Boost (runs at 7 watts no fan) Storage: One 512 GB SSD That is a boot drive and main drive; RAM: 8GB Single-Channel DDR3L 1600Mhz")
    await ctx.send(embed=embed)
mainClient.run(mainToken)