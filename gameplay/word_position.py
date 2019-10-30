def get_letter_group(letters, direction, col, row):
    return {'letters': letters, 
            'direction': direction, 
            'col': col, 
            'row': row
            'length': len(letters)}

def get_tile_lines(word_indx):

# given the current state of the board find all viable tiles to play a word around 
# (ex. a tile without tiles on its left or right, or top and bottom)
def word_position(board):
    word_indx = []
    playable = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j][0].isspace() and not board[i][j][1].isspace():
                word_indx.append([i, j])
                
    while i < len(word_indx):
        col = word_indx[i][0]
        row = word_indx[i][1]
        letters = [board[col][row]]
        nxt = col + 1
        for j in range(i + 1, len(word_indx)):
            if word_indx[j][0] != nxt:
                i = j
                break
            else:
                letters.append(board[nxt][row])
        letter_group = get_letter_group(letters, 'r', col, row)
        playable.append(letter_group)
    word_indx = sorted(word_indx, key=lambda x: x[1])
    while i < len(word_indx):
        col = word_indx[i][0]
        row = word_indx[i][1]
        letters = [board[col][row]]
        nxt = row + 1
        for j in range(i + 1, len(word_indx)):
            if word_indx[0][j] != nxt:
                i = j
                break
            else:
                letters.append(board[col][nxt])
        letter_group = get_letter_group(letters, 'd', col, row)
        playable.append(letter_group)




    # for pair in word_indx:
    #     i = pair[0]
    #     j = pair[1]
    #     if [i, j + 1] not in word_indx and [i, j - 1] not in word_indx:
    #         playable.append([i, j, 'r'])
    #     elif [i + 1, j] not in word_indx and [i - 1, j] not in word_indx:
    #        playable.append([i, j, 'd'])
    return playable 