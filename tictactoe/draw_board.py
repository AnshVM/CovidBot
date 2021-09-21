async def draw_board(message,grid):
    await message.channel.send('`'+grid[0]+' '+grid[1]+' '+grid[2]+'`')
    await message.channel.send('`'+grid[3]+' '+grid[4]+' '+grid[5]+'`')
    await message.channel.send('`'+grid[6]+' '+grid[7]+' '+grid[8]+'`')
