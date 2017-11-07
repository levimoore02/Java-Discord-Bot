import discord
import asyncio
import time
import os
from subprocess import Popen

client = discord.Client()

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('WRITE SCRIPT')
	print('------')

@client.event
async def on_message(message):
	args = [message.content, "info.txt"]
	if not message.content.startswith("@>"):
		
		text = args[0]
		args[1] = "info.txt";
		#Save file is "info.txt", which is user input
		saveFile = open(args[1], "w")
		saveFile.write(text)
		saveFile.close()
		#Start runJava BEFORE result.txt is required
		os.startfile("runJava.bat")
		time.sleep(1)
		file = open("result.txt", "r")
		printed = file.read()
		#Print contents of result.txt (output of java)
		await client.send_message(message.channel, "@>" + printed)
		time.sleep(1)
		#Clear result.txt
		open("result.txt", "w").close()
                
client.run('token')