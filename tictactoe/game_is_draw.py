def game_is_draw(grid):
    is_draw=False
    for i in range(0,9,1):
        if grid[i]=='X' or grid[i]=='O':
            is_draw=True
        else:
            is_draw=False
            break
    return is_draw

