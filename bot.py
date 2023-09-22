# bot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import googleAnalytics
from table2ascii import table2ascii as t2a

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.event
async def on_ready():
    print('Bot is ready')

    

@bot.command(name='views', help='Get viewer page visits')
async def getViews(
    ctx,
    startDate: str = commands.parameter(
        default="today",
        description="(NdaysAgo, yesterday, today, or YYYY-MM-DD)"
        ),
    endDate: str = commands.parameter(
        default="today",
        description="(NdaysAgo, yesterday, today, or YYYY-MM-DD)"
        )
    ):

    # get page views from Google Analytics
    response = googleAnalytics.getPageViews(
        startDate=startDate,
        endDate=endDate
    )

    # create table
    output = t2a(
        header = response[0],
        body = response[1:],
        first_col_heading=True
    )

    await ctx.send(f"```\n{output}\n```")



@bot.command(name='location', help='Get viewer location')
async def getLocations(
    ctx,
    type: str = commands.parameter(
        default="country",
        description="(continent, country, city, region)"
        ),
    startDate: str = commands.parameter(
        default="today",
        description="(NdaysAgo, yesterday, today, or YYYY-MM-DD)"
        ),
    endDate: str = commands.parameter(
        default="today",
        description="(NdaysAgo, yesterday, today, or YYYY-MM-DD)"
        )
    ):

    # get page views from Google Analytics
    response = googleAnalytics.getLocations(
        locationType=type,
        startDate=startDate,
        endDate=endDate
    )

    # create table
    output = t2a(
        header = response[0],
        body = response[1:],
        first_col_heading=True
    )

    await ctx.send(f"```\n{output}\n```")

bot.run(TOKEN)