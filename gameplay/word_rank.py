from itertools import combinations
from bisect import bisect_left
from word_position import word_position
import itertools

SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def load_vars():
    f = open('C:\\Users\\Laura\\Documents\\University\\5th Year Eng\\ENPH 454\\ScrabbleBot\\scrabble-brain\\gameplay\\anadict.txt', 'r')
    ana_dict = f.read().split('\n')
    f.close()
    return ana_dict


def score_word(word):
    return sum([SCORES[c] for c in word])


def find_words(rack, ana_dict, board_ltr):
    rack = ''.join(sorted(rack))
    found_words = []
    for i in range(1, len(rack)+1):
        for comb in combinations(rack, i):
            comb = (board_ltr,) + comb
            ana = ''.join(sorted(comb))
            j = bisect_left(ana_dict, ana)
            if j == len(ana_dict):
                continue
            words = ana_dict[j].split()
            if words[0] == ana:
                found_words.extend(words[1:])
    return found_words
# def play_row(play_info, word)
def word_dict(word, indx):
    return {'word': word,
            'score': score_word(word),
            'index': indx}

def get_game_play(word, playable, board):
    word_info = playable[word['index']]
    board_ltr = board[word_info[0]][word_info[1]]
    board_ltr = board_ltr.lower().strip()
    tiles = word['word'].split(board_ltr)
    row = word_info[1]
    col = word_info[0]
    if word_info[2] == 'right':
        row = row - len(tiles[0])
    elif word_info[2] == 'left':
        col = col - len(tiles[0])
    return {'word': word['word'],
            'col': col,
            'row': row,
            'direction': word_info[2]}

def word_rank(rack, board):
    board = [['TWS', '   ', '   ', 'DLS', '   ', '   ', '   ', 'TWS', '   ', '   ', '   ', 'DLS', '   ', '   ', 'TWS'], ['   ', 'DWS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'DWS', '   '], ['   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   '], ['DLS', '   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   ', 'DLS'], ['   ', '   ', '   ', '   ', 'DWS', '   ', '   ', '   ', '   ', '   ', 'DWS', '   ', '   ', '   ', '   '], ['   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   '], ['   ', '   ', 'DLS', '   ', '   ', '   ', 'DLS', '   ', 'DLS', '   ', '   ', '   ', 'DLS', '   ', '   '], ['TWS', '   ', '   ', 'DLS', '   ', '   ', '   ', ' R ', ' O ', ' A ', ' D ', 'DLS', '   ', '   ', 'TWS'], ['   ', '   ', 'DLS', '   ', '   ', '   ', ' W ', ' A ', ' T ', ' T ', '   ', '   ', 'DLS', '   ', '   '], ['   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', ' R ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   '], ['   ', '   ', '   ', '   ', ' J ', ' O ', ' K ', ' E ', '   ', '   ', 'DWS', '   ', '   ', '   ', '   '], ['DLS', '   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   ', 'DLS'], ['   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   '], ['   ', 'DWS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'DWS', '   '], ['TWS', '   ', '   ', 'DLS', '   ', '   ', '   ', 'TWS', '   ', '   ', '   ', 'DLS', '   ', '   ', 'TWS']]
    rack_new = rack.split(", ").copy()
    rack_new = [x.lower() for x in rack_new]
    playable = word_position(board)
    ana_dict = load_vars()
    scored = []
    for pair in playable:
        indx = 0
        board_ltr = board[pair[0]][pair[1]].lower().strip()
        found_words = set(find_words(rack_new, ana_dict, board_ltr))
        scores = [word_dict(word, indx) for word in found_words]
        scored.extend(scores)
        indx += 1
    scored = sorted(scored, key=lambda k: k['score'], reverse=True)
    game_play = get_game_play(scored[0], playable, board)
    print(game_play)