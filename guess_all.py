import random
async def guess_all(message,client):

    await message.channel.send('Guess a number from 1 and 10.')
    
    def is_correct(m):
        return m.content.isdigit()

    answer = random.randint(1, 10)
    correct = False
    

    while(not(correct)):
      
        msg = await client.wait_for("message",check=is_correct) 
        guess=msg.content
        n=int(guess)
        if n == answer:
            correct = True
            return await msg.reply("You are correct {0.mention}".format(msg.author))        
        else:
            await msg.reply("Try again")