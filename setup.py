import numpy as np

# (letter, multiplier, isLetter)
# isLetter - True => letter multiplier, False => word multiplier

def init_board():
    board = np.full(
        [15,15],
        {'letter': '', 'multiplier': 1, 'isLetter': True},
        dtype=object
    )

    # triple word multiplier
    board[0,0] = board[0,7] = board[0,14] = board[7,0] = board[7,14] = \
    board[14,0] = board[14,7] = board[14,14] = \
    {'letter': '', 'multiplier': 3, 'isLetter': False}

    # triple letter multiplier
    board[1,5] = board[1,9] = board[5,1] = board[5,5] = board[5,9] = \
    board[5,13] = board[9,1] = board[9,5] = board[9,9] = board[9,13] = \
    board[13,5] = board[13,9] = \
    {'letter': '', 'multiplier': 3, 'isLetter': True}

    # double word multiplier
    board[1,1] = board[2,2] = board[3,3] = board[4,4] = board[4,10] = \
    board[3,11] = board[2,12] = board[1,13] = board[10,4] = board[11,3] = \
    board[12,2] = board[13,1] = board[10,10] = board[11,11] = board[12,12] = \
    board[13,13] = board[7,7] = \
    {'letter': '', 'multiplier': 2, 'isLetter': False}

    # double letter multiplier
    board[0,3] = board[0,11] = board[2,6] = board[2,8] = board[3,0] = \
    board[3,7] = board[3,14] = board[6,2] = board[6,6] = board[6,8] = \
    board[6,12] = board[7,3] = board[7,11] = board[8,2] = board[8,6] = \
    board[8,8] = board[8,12] = board[11,0] = board[11,7] = board[11,14] = \
    board[12,6] = board[12,8] = board[14,3] = board[14,11] = \
    {'letter': '', 'multiplier': 2, 'isLetter': True}


    return board
