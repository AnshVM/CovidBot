from .draw_board import draw_board
from .game_is_draw import game_is_draw
from .get_id import get_id
from .p_winner import p_winner
from .get_input import get_input



async def tictactoe(message,client):
  
  player1 = await client.fetch_user(message.author.id)
  player2 = await client.fetch_user(get_id(message))

  await message.channel.send("{0.mention} has challenged {1.mention} for a game of TicTacToe".format(player1,player2))
  await message.channel.send("{0.mention} will play first as X.\n{1.mention} will play second as O".format(player1,player2))

  board = ['1','2','3','4','5','6','7','8','9']

  await draw_board(message,board)

  game_ended = False

  while not(game_ended):

    n = await get_input(message,client,player1,player2,board)
    board[n-1] = 'X'

    await draw_board(message,board)
    
    if(p_winner(board,'X')):
      await message.channel.send("{0.mention} has won the game".format(player1))
      game_ended = True
      break

    if(game_is_draw(board)):
      await message.channel.send("The game is draw")
      game_ended = True
      break

    n = await get_input(message,client,player2,player1,board)
    board[n-1] = 'O'

    await draw_board(message,board)
    
    if(p_winner(board,'O')):
      await message.channel.send("{0.mention} has won the game".format(player2))
      game_ended = True
      break

    if(game_is_draw(board)):
      await message.channel.send("The game is draw")
      game_ended = True
      break

    
    





