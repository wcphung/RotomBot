import discord
import datetime
import asyncio
import os
import pytz

TOKEN = os.environ.get('TOKEN')
SERVER_ID = os.environ.get('SERVER_ID')
tz = pytz.timezone('America/Los_Angeles')

client = discord.Client()

@client.event
async def on_message(message):
    server = client.get_server(SERVER_ID)
    author = message.author
    if author == client.user:
        return
    elif '!add Fenton' in message.content:
        role = discord.utils.get(server.roles, name='Fenton')
        if role in author.roles:
            response = '{0.author.mention} you are already notified of Fenton raids. No changes have been made'.format(message)
            await client.send_message(message.channel, response)
        elif role not in author.roles:
            response = '{0.author.mention} you have been ADDED to Fenton raid notifications'.format(message)
            await client.add_roles(author, role)
            await client.send_message(message.channel, response)
    elif "!remove Fenton" in message.content:
        role = discord.utils.get(server.roles, name='Fenton')
        if role in author.roles:
            response = '{0.author.mention} you have been REMOVED from Fenton raid notifications'.format(message)
            await client.remove_roles(author, role)
            await client.send_message(message.channel, response)
        elif role not in author.roles:
            response = '{0.author.mention} you already do NOT get Fenton raid notifications. No changes have been made'.format(message)
            await client.send_message(message.channel, response)
    elif '!add Civita' in message.content:
        role = discord.utils.get(server.roles, name='Civita')
        if role in author.roles:
            response = '{0.author.mention} you are already notified of Civita raids. No changes have been made'.format(message)
            await client.send_message(message.channel, response)
        elif role not in author.roles:
            response = '{0.author.mention} you have been ADDED to Civita raid notifications'.format(message)
            await client.add_roles(author, role)
            await client.send_message(message.channel, response)
    elif "!remove Civita" in message.content:
        role = discord.utils.get(server.roles, name='Civita')
        if role in author.roles:
            response = '{0.author.mention} you have been REMOVED from Civita raid notifications'.format(message)
            await client.remove_roles(author, role)
            await client.send_message(message.channel, response)
        elif role not in author.roles:
            response = '{0.author.mention} you already do NOT get Civita raid notifications. No changes have been made'.format(message)
            await client.send_message(message.channel, response)
    elif '!add AnyMVRaid' in message.content:
        role = discord.utils.get(server.roles, name='AnyMVRaid')
        if role in author.roles:
            response = '{0.author.mention} you are already notified of AnyMVRaid raids. No changes have been made'.format(message)
            await client.send_message(message.channel, response)
        elif role not in author.roles:
            response = '{0.author.mention} you have been ADDED to AnyMVRaid raid notifications'.format(message)
            await client.add_roles(author, role)
            await client.send_message(message.channel, response)
    elif "!remove AnyMVRaid" in message.content:
        role = discord.utils.get(server.roles, name='AnyMVRaid')
        if role in author.roles:
            response = '{0.author.mention} you have been REMOVED from AnyMVRaid raid notifications'.format(message)
            await client.remove_roles(author, role)
            await client.send_message(message.channel, response)
        elif role not in author.roles:
            response = '{0.author.mention} you already do NOT get AnyMVRaid raid notifications. No changes have been made'.format(message)
            await client.send_message(message.channel, response)

async def set_mentionable():
    await client.wait_until_ready()
    # set each role
    server = client.get_server(SERVER_ID)
    admin_role = discord.utils.get(server.roles, name='Moderators')
    fenton_role = discord.utils.get(server.roles, name='Fenton')
    civita_role = discord.utils.get(server.roles, name='Civita')
    anymvraid_role = discord.utils.get(server.roles, name='AnyMVRaid')
    #loop to check the time and turn @Mentions on/off
    while not client.is_closed:
        current_hour = datetime.datetime.now(tz).hour
        print('The current hour is ' + str(current_hour))
        print('This current datetime is ' + str(datetime.datetime.now(tz)))
        if current_hour >= 23 or current_hour <= 6:
                if admin_role.mentionable:
                    await client.edit_role(server, admin_role, mentionable=False)
                    print('Moderator mentions off')
                else:
                    print('No Moderator changes needed for 11pm-6am')
                if fenton_role.mentionable:
                    await client.edit_role(server, fenton_role, mentionable=False)
                    print('Fenton mentions off')
                else:
                    print('No Fenton changes needed for 11pm-6am')
                if civita_role.mentionable:
                    await client.edit_role(server, civita_role, mentionable=False)
                    print('Civita Mentions off')
                else:
                    print('No Civita changes needed for 11pm-6am')
                if anymvraid_role.mentionable:
                    await client.edit_role(server, anymvraid_role, mentionable=False)
                    print('AnyMVRaid mentions off')
                else:
                    print('No AnyMVRaid changes needed for 11pm-6am')
        else:
            if not admin_role.mentionable:
                await client.edit_role(server, admin_role, mentionable=True)
                print('Moderator mentions on')
            else:
                print('No Moderator changes needed for 6am-11pm')
            if not fenton_role.mentionable:
                await client.edit_role(server, fenton_role, mentionable=True)
                print('Fenton mentions on')
            else:
                print('No Fenton changes needed for 6am-11pm')
            if not civita_role.mentionable:
                await client.edit_role(server, civita_role, mentionable=True)
                print('Civita mentions on')
            else:
                print('No Civita changes needed for 6am-11pm')
            if not anymvraid_role.mentionable:
                await client.edit_role(server, anymvraid_role, mentionable=True)
                print('AnyMVRaid mentions on')
            else:
                print('No AnyMVRaid changes needed for 6am-11pm')
        print('------')
        #perform every hour = 3600 seconds
        await asyncio.sleep(3600)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    print('Servers connected to:')
    for server in client.servers:
        print(server.name)
    print('------')

client.loop.create_task(set_mentionable())
client.run(TOKEN)
