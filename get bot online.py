#importing the discord module
import discord
client=discord.Client()
@client.event
async def on_ready():
    print('Logged in')
    print("Username: ",end='')
    print(client.user.name)
    print("Userid: ",end='')
    print(client.user.id)
@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return
    if message.content.startswith('Hi') or message.content.startswith('Hello'):
        await message.channel.send('Hello {0.author.mention} Welcome Man'.format(message))
    elif message.content.startswith('help'):
        await message.channel.send("Let me check with that level and come back to you")
client.run('your token_id')
