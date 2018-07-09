import discord
import random
import asyncio
import requests


client = discord.Client()
DEIN_USERNAME = "192794157842956290"
testmsgid = None
testmsguser = None


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    await client.change_presence(game=discord.Game(name="?role")),


@client.event
async def on_message(message):
   if message.content.lower().startswith('?coin'):  # Coinflip 50/50% chance kopf oder zahl
     choice = random.randint(1, 2)
     if choice == 1:
       await client.add_reaction(message, '🌑')
     if choice == 2:
       await client.add_reaction(message, '🌕'),


   if message.content.startswith('!clear'):
       for role in message.author.roles:
         if role.name == "Admin":
          await client.send_message(message.channel, 'Clearing messages...')
          async for msg in client.logs_from(message.channel):
           await client.delete_message(msg)


   if message.content.lower().startswith("?role"):

     await client.send_message(message.channel, "**SELF  Roler**")
     await client.send_message(message.channel, "----------------------------------------------------------------------------------------------------")
     botmsg = await client.send_message(message.channel, "🇪🇺  EU or 🇺🇸  NA   -   🇪cho Arena or 🇹he Unspoken or 🇸print Vector or 🇴nward")
     await client.send_message(message.channel, "----------------------------------------------------------------------------------------------------\n"
                                                "Add your role's by click on reactions or remove them with 🆑\n"
                                                "**Notice Only add the roles that are based on facts!**\n"
                                                "-----------------------------------------------------------------------------------------------------")


     await client.add_reaction(botmsg, "🇪🇺")
     await client.add_reaction(botmsg, "🇺🇸")
     await client.add_reaction(botmsg, "🇪")
     await client.add_reaction(botmsg, "🇹")
     await client.add_reaction(botmsg, "🇸")
     await client.add_reaction(botmsg, "🇴")
     await client.add_reaction(botmsg, "🆑")

     global testmsgid
     testmsgid = botmsg.id

     global testmsguser
     testmsguser = message.author

@client.event
async def on_reaction_add(reaction, user):
   msg = reaction.message
   chat = reaction.message.channel

   if reaction.emoji == "🇪🇺" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "EU", msg.server.roles)
        await client.add_roles(user, role)
        await client.send_message(chat, "```Role EU added```")

   if reaction.emoji == "🇺🇸" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "NA", msg.server.roles)
        await client.add_roles(user, role)
        await client.send_message(chat, "```Role NA added```")

   if reaction.emoji == "🇪" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "Echo Arena", msg.server.roles)
        await client.add_roles(user, role)
        await client.send_message(chat, "```Role Echo Arena added```")

   if reaction.emoji == "🇹" and msg.id == testmsgid and user == testmsguser:
       role = discord.utils.find(lambda r: r.name == "The Unspoken", msg.server.roles)
       await client.add_roles(user, role)
       await client.send_message(chat, "```Role The Unspoken added```")

   if reaction.emoji == "🇸" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "Sprint Vector", msg.server.roles)
        await client.add_roles(user, role)
        await client.send_message(chat, "```Role Sprint Vector added```")

   if reaction.emoji == "🇴" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "Onward", msg.server.roles)
        await client.add_roles(user, role)
        await client.send_message(chat, "```Role Onward added```")

   if reaction.emoji == "🆑" and msg.id == testmsgid and user == testmsguser:
        role = discord.utils.find(lambda r: r.name == "EU", msg.server.roles)
        await client.remove_roles(user, role)
        # await client.send_message(chat, "Role removed")
        role2 = discord.utils.find(lambda r2: r2.name == "NA", msg.server.roles)
        await client.remove_roles(user, role2)
        # await client.send_message(chat, "Role removed")
        role3 = discord.utils.find(lambda r3: r3.name == "Echo Arena", msg.server.roles)
        await client.remove_roles(user, role3)
        # await client.send_message(chat, "Role removed")
        role4 = discord.utils.find(lambda r4: r4.name == "The Unspoken", msg.server.roles)
        await client.remove_roles(user, role4)
        # await client.send_message(chat, "Role removed")
        role5 = discord.utils.find(lambda r5: r5.name == "Sprint Vector", msg.server.roles)
        await client.remove_roles(user, role5)
        # await client.send_message(chat, "Role removed")
        role6 = discord.utils.find(lambda r6: r6.name == "Onward", msg.server.roles)
        await client.remove_roles(user, role6)
        await client.send_message(chat, "```Role(s) removed```")




async def tutorial_uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1
    #client.loop.create_task(tutorial_uptime())

client.loop.create_task(tutorial_uptime())


client.run('NDYwMzI3ODc3MTcxMjE2Mzk0.DhEgKQ.zG531Mop6PuJr_kSt8VHUPrO3XQ')
