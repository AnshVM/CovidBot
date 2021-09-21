import asyncio
import random

async def guess(message,client):

    await message.channel.send('Guess a number between 1 and 10.')
    
    def is_correct(m):
        return m.author == message.author and m.content.isdigit()

    answer = random.randint(1, 10)
    correct = False
    

    while(not(correct)):
      
        try:
            n = await client.wait_for("message",timeout=20.0,check=is_correct)        
        except asyncio.TimeoutError:
            return await message.channel.send("Sorry you had only 20 seconds")
        
        if int(n.content) == answer:
            correct = True
            return await message.channel.send("You are correct!!")        
        else:
            await message.channel.send("Try again")