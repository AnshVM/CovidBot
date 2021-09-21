async def hello(message):
  await message.reply("Hello {0.mention}".format(message.author))



