def get_letter_group(letters, direction, col, row):
    return {'letters': letters, 
            'direction': direction, 
            'col': col, 
            'row': row,
            'length': len(letters)}

def get_tile_lines(word_indx, board):
    playable = []
    i = 0
    #need to teminate one round earlier
    while i < len(word_indx):
        col = word_indx[i][0]
        row = word_indx[i][1]
        letters = [board[col][row].strip()]
        if i == len(word_indx) - 1:
            letter_group = get_letter_group(letters, 'r', col, row)
            playable.append(letter_group)
            break
        nxt = col + 1
        for j in range(i + 1, len(word_indx)):
            if word_indx[j][1] == nxt and word_indx[j][0] == row:
                letters.append(board[row][nxt].strip())
                nxt += 1
                if j == len(word_indx) - 1:
                    i = j + 1
            else:
                i = j
                break
        letter_group = get_letter_group(letters, 'r', col, row)
        playable.append(letter_group)
    word_indx = sorted(word_indx, key=lambda x: x[1])
    i = 0
    while i < len(word_indx):
        col = word_indx[i][0]
        row = word_indx[i][1]
        letters = [board[col][row]]
        if i == len(word_indx) - 1:
            letter_group = get_letter_group(letters, 'd', col, row)
            playable.append(letter_group)
            break
        nxt = row + 1
        for j in range(i + 1, len(word_indx)):
            if word_indx[j][0] == nxt and word_indx[j][1] == col:
                letters.append(board[nxt][col].strip())
                nxt += 1
                if j == len(word_indx) - 1:
                    i = j + 1
            else:
                i = j
                break
        letter_group = get_letter_group(letters, 'd', col, row)
        playable.append(letter_group)
    return playable

# given the current state of the board find all viable tiles to play a word around 
# (ex. a tile without tiles on its left or right, or top and bottom)
def word_position(board):
    word_indx = []
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j][0].isspace() and not board[i][j][1].isspace():
                word_indx.append([i, j])
    playable = get_tile_lines(word_indx, board)
    print(playable)
    return playable 