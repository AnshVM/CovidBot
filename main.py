import discord
import os

from server import keep_alive

from hello import hello
from guess import guess
from tictactoe.tictactoe import tictactoe
from covid import covid
from guess_all import guess_all

client = discord.Client() #Represents a client connection that connects to Discord. This class is used to interact with the Discord

@client.event #registers an event to listen to.
async def on_ready(): #called when bot is ready
  print("Logged in")

@client.event 
async def on_message(message): #called when a message is sent to the server

  if(message.content == "oy hello"):
    await hello(message)

  if(message.content == "oy guess"):
    await guess(message,client)

  if(message.content == "oy guess all"):
    await guess_all(message,client)

  if(message.content.startswith("oy tictactoe")):
    await tictactoe(message,client)

  if(message.content.startswith("oy covid")):
    await covid(message)



keep_alive()
client.run(os.getenv("TOKEN"))




