import numpy as np

letter_scores = {
    'a': 9,
    'b': 2,
    'c': 2,
    'd': 4,
    'e': 12,
    'f': 2,
    'g': 3,
    'h': 2,
    'i': 9,
    'j': 1,
    'k': 1,
    'l': 4,
    'm': 2,
    'n': 6,
    'o': 8,
    'p': 2,
    'q': 1,
    'r': 6,
    's': 4,
    't': 6,
    'u': 4,
    'v': 2,
    'w': 2,
    'x': 1,
    'y': 2,
    'z': 1
}

def calc_word_score(start_idx, end_idx, pos, is_vertical, board):
    score = 0
    word_multiplier = 1;
    for i in range(start_idx, end_idx+1):
        if (is_vertical):
            tile = board[i, pos]
        else:
            tile = board[pos, i]

        try:
            tile_score = letter_scores[tile['letter']]
        except:
            print("No letter found")

        if (tile['isLetter']):
            tile_score *= tile['multiplier']
        else:
            word_multiplier *= tile['multiplier']

        score += tile_score

    return score * word_multiplier
