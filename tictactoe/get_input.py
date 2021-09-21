import asyncio

async def get_input(message,client,player,other_player,grid):

  await message.channel.send("{0.mention} its your turn. Choose a cell to occupy".format(player))

  def check(m):
    return m.author.id == player.id and m.content.isdigit()         

  valid_input = False

  while not(valid_input):

    try:
      msg = await client.wait_for("message",check=check,timeout = 60.0)
    except asyncio.TimeoutError:
      return await message.channel.send("{0.mention} didnt reply in 60 seconds.\n{1.mention} has won the game".format(player,other_player))
    
    n=int(msg.content)

    if(n>9 or n<1):
      await message.channel.send("You must enter a number from 1 to 9 only.\nEnter again")
      continue;

    elif(grid[n-1].isdigit() == False):
      await message.channel.send("This cell has already been occupied")

    else:
      valid_input = True
      return n
    


