import discord, getdata, time, datetime, asyncio, asyncpg
from discord.ext import commands, tasks
from discord import Member
from discord.utils import get

count = 1
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '!' ,intents=intents)
client.remove_command('help')
sent = False
updated = False

async def updatePodium():
    await client.wait_until_ready()
    # general channel = 705519423146164246 , Bot_test channel = 780124613593006090
    channel = client.get_channel(787797996137218049)
    msg1 = getdata.getHighestMmr(38)
    msg2 = getdata.getHighestMmr(42)
    msg3 = getdata.getHighestMmr(46)
    await channel.send(str(msg1))
    await channel.send(str(msg2))
    await channel.send(str(msg3))

@tasks.loop(minutes=1,count=None)
async def checkDate():
    global sent
    global updated
    now = datetime.datetime.now()
    weekday = now.weekday()
    hour = now.hour
    minute = now.minute
    if now.weekday() == 0:
        day = 'Monday'
    elif now.weekday() == 1:
        day = 'Tuesday'
    elif now.weekday() == 2:
        day = 'Wednesday'
    elif now.weekday() == 3:
        day = 'Thursday'
    elif now.weekday() == 4:
        day = 'Friday'
    elif now.weekday() == 5:
        day = 'Saturday'
    elif now.weekday() == 6:
        day = 'Sunday'
    channel = client.get_channel(780124613593006090)
    count = 0
    startat = 1
    #Weekday : 0 - Monday , ... 6 - Sunday
    if weekday == 6 and not sent and hour == 20 and minute == 0:
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        await channel.send('Server time: '+ dt_string)
        await channel.send('Today is: ' + day)
        await channel.send('Updating the Champions!')
        await updatePodium()
        sent = True
    elif weekday != 6:
        sent = False
    if hour % 6 == 0 and not updated:
        updated = True
        guild = client.get_guild(id=567072320200507471)
        for member in guild.members:
            count += 1
            startat += 1
            col = 1
            getdata.getAll(startat , col, str(member))
            col = 2
            getdata.getAll(startat , col, str(member.id))
        await channel.send('Number of users: '+ str(count))
        await channel.send('Google Sheet updated!')
    elif 6 % 2 > 0:
        updated = False

@client.event
async def on_ready():
    checkDate.add_exception_type(asyncpg.PostgresConnectionError)
    checkDate.start()
    now = datetime.datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print('[ ' + dt_string + ' ] - Bot online.')

@client.command()
async def hi(ctx):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        await ctx.send('Hello Stranger! I am happy to be alive back again!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')
    
    
@client.command()
async def getall(ctx):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        count = 0
        startat = 1
        async for m in ctx.guild.fetch_members():    
                count += 1
                startat += 1
                col = 1
                getdata.getAll(startat , col, str(m))
                col = 2
                getdata.getAll(startat , col, str(m.id))
        await ctx.send('Number of users: '+ str(count))
        await ctx.send('Google Sheet updated!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command()
async def rank2s(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add argument! ex: !rank2s User')
        else:
            try:
                cell = 'A14'
                getdata.updateCell(cell,str(arg))
                val = getdata.wks.acell('B14').value
                await ctx.send(val)
            except Exception as e:
                print('Could not find: ' +e)
                await ctx.send('User not found!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command()
async def rank1s(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add argument! ex: !rank1s User')
        else:
            try:
                cell = 'A10'
                getdata.updateCell(cell,str(arg))
                val = getdata.wks.acell('B10').value
                await ctx.send(val)
            except Exception as e:
                print('Could not find: ' +e)
                await ctx.send('User not found!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command()
async def rank3s(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add argument! ex: !rank1s User')
        else:
            try:
                cell = 'A18'
                getdata.updateCell(cell,str(arg))
                val = getdata.wks.acell('B18').value
                await ctx.send(val)
            except Exception as e:
                print('Could not find: ' +e)
                await ctx.send('User not found!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command()
async def rank(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add argument! ex: !rank User')
        else:
            try:
                cell = 'A22'
                getdata.updateCell(cell,str(arg))
                val = getdata.wks.acell('B22').value
                await ctx.send(val)
            except Exception as e:
                print('Could not find: ' +e)
                await ctx.send('User not found!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command()
async def country(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add argument! ex: !country User')
        else:
            try:
                cell = 'A26'
                getdata.updateCell(cell,str(arg))
                val = getdata.wks.acell('B26').value
                await ctx.send(val)
            except Exception as e:
                print('Could not find: ' +e)
                await ctx.send('User not found!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command(pass_context=True)
async def matchmake(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add argument! ex: !matchmake country or !matchmake rank')
        elif arg == 'country':
            cell = 'A30'
            getdata.updateCell(cell,str(ctx.message.author.mention))
            val = getdata.wks.acell('B30').value
            await ctx.send('Players from the same country as you:\n' +val)
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command(pass_context=True)
async def addfriend(ctx , arg=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None:
            await ctx.send('Please add a user id ex: !addfriend User#1234')
        else:
            cell = 'B34'
            getdata.updateCell(cell,str(arg))
            getdata.wks.update('A34',ctx.message.author.mention)
            val = getdata.wks.acell('C34').value
            await ctx.send(val)
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command()
async def whostronger(ctx , arg=None, arg2=None):
    channel = ctx.message.channel
    if channel.id == 780185249782956042 or channel.id == 780124613593006090:
        if arg == None or arg2 == None:
            await ctx.send('Please add argument! ex:\n!whostronger ones User#1234\n!whostronger twos User#1234\n!whostronger threes User#1234')
        else:
            try:
                if arg == 'ones':
                    user_id = ctx.message.author.id
                    user = '<@!{}>'.format(user_id)
                    cell = 'A50'
                    getdata.updateCell(cell,str(user))
                    cell = 'B50'
                    getdata.updateCell(cell,str(arg2))
                    user2 = getdata.wks.acell('B50').value
                    msg = getdata.wks.acell('C50').value
                    msg2 = msg.replace('#I1D', str(user))
                    editedmsg = msg2.replace('#I2D', str(user2))
                    await ctx.send(editedmsg)
                elif arg == 'twos':
                    user_id = ctx.message.author.id
                    user = '<@!{}>'.format(user_id)
                    cell = 'A54'
                    getdata.updateCell(cell,str(user))
                    cell = 'B54'
                    getdata.updateCell(cell,str(arg2))
                    user2 = getdata.wks.acell('B54').value
                    msg = getdata.wks.acell('C54').value
                    msg2 = msg.replace('#I1D', str(user))
                    editedmsg = msg2.replace('#I2D', str(user2))
                    await ctx.send(editedmsg)
                elif arg == 'threes':
                    user_id = ctx.message.author.id
                    user = '<@!{}>'.format(user_id)
                    cell = 'A58'
                    getdata.updateCell(cell,str(user))
                    cell = 'B58'
                    getdata.updateCell(cell,str(arg2))
                    user2 = getdata.wks.acell('B58').value
                    msg = getdata.wks.acell('C58').value
                    msg2 = msg.replace('#I1D', str(user))
                    editedmsg = msg2.replace('#I2D', str(user2))
                    await ctx.send(editedmsg)
            except Exception as e:
                print('Could not find: ' + str(e))
                await ctx.send('User not found!')
    else:
        await ctx.send('Please use the commands in #fred-commands !')

@client.command(pass_context=True)
async def help(ctx):
    channel = client.get_channel(788152206616428584)
    author = ctx.message.author
    embed = discord.Embed(colour = discord.Colour.orange())
    embed.set_author(name='Help')
    embed.add_field(name='!addfriend', value='Returns directly the link of a given user to add them to friends!\nExample:\n!addfriend @someone', inline=False)
    embed.add_field(name='!country', value='Returns the country of a given user\nExample:\n!country @someone', inline=False)
    embed.add_field(name='!hi', value='Returns a funny message from the bot\nExample:\n!hi ', inline=False)
    embed.add_field(name='!matchmake', value='Returns players that are matching by country\nExample:\n!matchmake country', inline=False)
    embed.add_field(name='!rank', value='Returns the rank from all 3 playlists of a given user\nExample:\n!rank @someone', inline=False)
    embed.add_field(name='!rank1s', value='Returns the rank from 1s playlist of a given user\nExample:\n!rank1s @someone', inline=False)
    embed.add_field(name='!rank2s', value='Returns the rank from 2s playlist of a given user\nExample:\n!rank2s @someone', inline=False)
    embed.add_field(name='!rank3s', value='Returns the rank from 3s playlist of a given user\nExample:\n!rank3s @someone', inline=False)
    embed.add_field(name='!whostronger', value='Returns the result of comparison between you and the given user\nExample:\n!whostronger @someone', inline=False)
    await author.send(embed=embed)
    await channel.send(embed=embed)

client.run('Nzc5NzEwMjAxOTI1OTkyNDgw.X7kftg.7A5qjUQYbqjtDxMtkOCJtkpB43U')