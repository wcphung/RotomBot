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
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

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
        if current_hour >= 23 or current_hour <= 7:
                if admin_role.mentionable:
                    await client.edit_role(server, admin_role, mentionable=False)
                    print('Moderator mentions off')
                else:
                    print('No Moderator changes needed for 11pm-8am')
                if fenton_role.mentionable:
                    await client.edit_role(server, fenton_role, mentionable=False)
                    print('Fenton mentions off')
                else:
                    print('No Fenton changes needed for 11pm-8am')
                if civita_role.mentionable:
                    await client.edit_role(server, civita_role, mentionable=False)
                    print('Civita Mentions off')
                else:
                    print('No Civita changes needed for 11pm-8am')
                if anymvraid_role.mentionable:
                    await client.edit_role(server, anymvraid_role, mentionable=False)
                    print('AnyMVRaid mentions off')
                else:
                    print('No AnyMVRaid changes needed for 11pm-8am')
        else:
            if not admin_role.mentionable:
                await client.edit_role(server, admin_role, mentionable=True)
                print('Moderator mentions on')
            else:
                print('No Moderator changes needed for 8am-11pm')
            if not fenton_role.mentionable:
                await client.edit_role(server, fenton_role, mentionable=True)
                print('Fenton mentions on')
            else:
                print('No Fenton changes needed for 8am-11pm')
            if not civita_role.mentionable:
                await client.edit_role(server, civita_role, mentionable=True)
                print('Civita mentions on')
            else:
                print('No Civita changes needed for 8am-11pm')
            if not anymvraid_role.mentionable:
                await client.edit_role(server, anymvraid_role, mentionable=True)
                print('AnyMVRaid mentions on')
            else:
                print('No AnyMVRaid changes needed for 8am-11pm')
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
