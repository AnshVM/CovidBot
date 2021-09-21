def p_winner(grid,player):
    b=False
    if grid[0]==player and grid[1]==player and grid[2]==player:
        b=True
    elif grid[3]==player and grid[4]==player and grid[5]==player:
        b=True
    elif grid[6]==player and grid[7]==player and grid[8]==player:
        b=True
    elif grid[0]==player and grid[3]==player and grid[6]==player:
        b=True
    elif grid[1]==player and grid[4]==player and grid[7]==player:
        b=True
    elif grid[2]==player and grid[5]==player and grid[8]==player:
        b=True
    elif grid[0]==player and grid[4]==player and grid[8]==player:
        b=True
    elif grid[2]==player and grid[4]==player and grid[6]==player:
        b=True
    return b
