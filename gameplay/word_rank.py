from itertools import combinations
from bisect import bisect_left
from word_position import word_position
import scrabble

# Scores for playing letters 
SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}

# Load words from the anagram text file
def load_vars():
    f = open('anadict.txt', 'r')
    ana_dict = f.read().split('\n')
    f.close()
    return ana_dict

#  Find individual scores for a list of words
def score_word(word):
    return sum([SCORES[c] for c in word])

# Find anagrams of all possible combanations of the rack,
# always including a letter on the board
def find_words(rack, ana_dict, board_ltr):
    rack = ''.join(sorted(rack))
    found_words = []
    for i in range(1, len(rack)+1):
        for comb in combinations(rack, i):
            if board_ltr != '':
                comb = (board_ltr,) + comb
            ana = ''.join(sorted(comb))
            j = bisect_left(ana_dict, ana)
            if j == len(ana_dict):
                continue
            words = ana_dict[j].split()
            if words[0] == ana:
                found_words.extend(words[1:])
    return found_words

# Format playable word with information needed to play
def word_dict(word, indx):
    return {'word': word,
            'score': score_word(word),
            'index': indx}

# Given a playable word calculate location to place the fist letter
def get_game_play(word, playable, board):
    word_info = playable[word['index']]
    board_ltr = board[word_info[0]][word_info[1]]
    board_ltr = board_ltr.lower().strip()
    ltr_split = word['word'].split(board_ltr)
    row = word_info[0]
    col = word_info[1]
    # In the case of the first turn where there aren't words to play around 
    if len(ltr_split[0]) == len(word['word']):
        ltr_split[0] = ''
    # On all other turns position the starting letter such that 
    # the letters already on the board line up with the word
    else:
        if word_info[2] == 'r':
            col = col - len(ltr_split[0])
        elif word_info[2] == 'd':
            row = row - len(ltr_split[0])
    return {'word': word['word'],
            'col': col,
            'row': row,
            'direction': word_info[2]}

#  Find list of playable words given a list of valid positions
#  returns list of words sorted by highest score
def get_top_words(playable, board, rack):
    ana_dict = load_vars()
    scored = []
    indx = 0
    for pair in playable:
        # Check to see if it is the first turn (no board letters to play around)
        if board[7][7] == ' * ':
            board_ltr = ''
        else:
            board_ltr = board[pair[0]][pair[1]].lower().strip()
        found_words = set(find_words(rack, ana_dict, board_ltr))
        scores = [word_dict(word, indx) for word in found_words]
        scored.extend(scores)
        indx += 1
    return sorted(scored, key=lambda k: k['score'], reverse=True)

# Check if word can be played on the board
def word_check(word, board, round_number, players):
    word_to_play = scrabble.Word(word['word'], [word['row'], word['col']], players[1], word['direction'], board)
    return word_to_play.check_word(round_number, players)

# Given a players rack and the board find the highest scoring valid 
# word to play and return information needed to play
def word_rank(rack, board, round_number, players):
    mod_rack = rack.split(", ").copy()
    mod_rack = [x.lower() for x in mod_rack]
    playable = word_position(board)
    scored = get_top_words(playable, board, mod_rack)
    check = False
    word_indx = 0
    while check != True:
        word_to_play = get_game_play(scored[word_indx], playable, board)
        check = word_check(word_to_play, board, round_number, players)
        print(word_to_play, check)
        word_indx += 1
    return word_to_play