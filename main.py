import discord
import os
from discord.ext import commands
import getdata
from discord import Member

count = 1
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!' ,intents=intents)

@client.event
async def on_ready():
    print('Bot online.')

@client.command()
async def hi(ctx):
    await ctx.send('Hello Stranger! I am happy to be alive back again!')

@client.command()
async def find(ctx, arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !find User')
    else:
        try:
            getdata.finduser(arg)
            await ctx.send('Found: '+ arg)
        except Exception as e:
            print('Could not find: ' +e)
            await ctx.send('User not found, please contact a moderator!')
    
@client.command()
async def getall(ctx):
    async for m in ctx.guild.fetch_members():
            await ctx.send(m.id)

@client.command()
async def test(ctx):
    count = 0
    startat = 26
    async for m in ctx.guild.fetch_members():
            count += 1
            startat += 1
            getdata.writecellA(startat , str(m))
            getdata.writecellB(startat , str(m.id))
    await ctx.send('Number of users: '+ str(count))
    await ctx.send('Google Sheet updated!')

@client.command()
async def rank2s(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !rank2s User')
    else:
        try:
            getdata.checkrank2s(str(arg))
            val = getdata.wks.acell('B14').value
            await ctx.send(val)
        except Exception as e:
            print('Could not find: ' +e)
            await ctx.send('User not found!')

@client.command()
async def rank1s(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !rank1s User')
    else:
        try:
            getdata.checkrank1s(str(arg))
            val = getdata.wks.acell('B10').value
            await ctx.send(val)
        except Exception as e:
            print('Could not find: ' +e)
            await ctx.send('User not found!')

@client.command()
async def rank3s(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !rank1s User')
    else:
        try:
            getdata.checkrank3s(str(arg))
            val = getdata.wks.acell('B18').value
            await ctx.send(val)
        except Exception as e:
            print('Could not find: ' +e)
            await ctx.send('User not found!')

@client.command()
async def rank(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !rank User')
    else:
        try:
            getdata.checkrank(str(arg))
            val = getdata.wks.acell('B22').value
            await ctx.send(val)
        except Exception as e:
            print('Could not find: ' +e)
            await ctx.send('User not found!')

@client.command()
async def country(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !country User')
    else:
        try:
            getdata.checkcountry(str(arg))
            val = getdata.wks.acell('B26').value
            await ctx.send(val)
        except Exception as e:
            print('Could not find: ' +e)
            await ctx.send('User not found!')

@client.command(pass_context=True)
async def matchmake(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add argument! ex: !matchmake country or !matchmake rank')
    elif arg == 'country':
        getdata.matchmake(str(ctx.message.author.mention))
        val = getdata.wks.acell('B30').value
        await ctx.send('Players from the same country as you:\n' +val)

@client.command(pass_context=True)
async def addfriend(ctx , arg=None):
    if arg == None:
        await ctx.send('Please add a user id ex: !addfriend User#1234')
    else:
        getdata.addfriend(str(arg))
        getdata.wks.update('A34',ctx.message.author.mention)
        val = getdata.wks.acell('C34').value
        await ctx.send(val)

client.run('Nzc5NzEwMjAxOTI1OTkyNDgw.X7kftg.7A5qjUQYbqjtDxMtkOCJtkpB43U')