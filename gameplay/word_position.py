import string 

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
            playable.append([i, j, 'r'])
        elif [i + 1, j] not in word_indx and [i - 1, j] not in word_indx:
           playable.append([i, j, 'd'])
    return playable 