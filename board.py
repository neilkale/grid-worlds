from enum import Enum

class ACTION(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4

board = [[]]

def read_board(fileName):
    pass

def print_board():
    pass

# Returns the new state (board position) reached by taking action a from state s
# TODO: Add probabilistic movement, 2 steps forward.
def next_state(s,a):
    row = s[0]
    col = s[1]
    if   (a == ACTION.LEFT):
        col -= 1
    elif (a == ACTION.RIGHT):
        col += 1
    elif (a == ACTION.UP):
        row -= 1
    elif (a == ACTION.DOWN):
        row += 1
    
    if (row < 0): row += 1
    if (col < 0): col += 1
    if (row > len(board)): row -= 1
    if (row > len(board[0])): col -= 1

    s[0] = row
    s[1] = col

    return s


