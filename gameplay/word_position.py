# given the current state of the board find all viable tiles to play a word around 
# (ex. a tile without tiles on its left or right, or top and bottom)
def word_position(board):
    word_indx = []
    playable = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j][0].isspace() and not board[i][j][1].isspace():
                word_indx.append([i, j])
    for pair in word_indx:
        i = pair[0]
        j = pair[1]
        if [i, j + 1] not in word_indx and [i, j - 1] not in word_indx:
            playable.append([i, j, 'right'])
        elif [i + 1, j] not in word_indx and [i - 1, j] not in word_indx:
           playable.append([i, j, 'down'])
    return playable 