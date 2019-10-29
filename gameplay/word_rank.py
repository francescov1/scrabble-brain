from itertools import combinations
from bisect import bisect_left
from word_position import word_position
import scrabble
import time

# TODO incorperate blank tiles and premium squares to algorithm, randomly breaks probably should look into that
# look into fixing error that happens when a space is in the word

# Load words from the anagram text file
def load_vars():
    f = open('anadict.txt', 'r')
    ana_dict = f.read().split('\n')
    f.close()
    return ana_dict

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

# Given a playable word calculate location to place the fist letter
def get_word(word, indx, playable, board, players):
    word_info = playable[indx]
    board_ltr = board[word_info[0]][word_info[1]]
    board_ltr = board_ltr.lower().strip()
    ltr_split = word.split(board_ltr)
    row = word_info[0]
    col = word_info[1]
    # In the case of the first turn where there aren't words to play around 
    if len(ltr_split[0]) == len(word):
        ltr_split[0] = ''
    # On all other turns position the starting letter such that 
    # the letters already on the board line up with the word
    else:
        if word_info[2] == 'r':
            col = col - len(ltr_split[0])
        elif word_info[2] == 'd':
            row = row - len(ltr_split[0])
    return scrabble.Word(word, [row, col], players[1], word_info[2], board)

#  Find list of playable words given a list of valid positions
#  returns list of words sorted by highest score
def get_top_words(playable, board, rack, players):
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
        # put word objects
        scored = []
        for word in found_words:
            word_obj = get_word(word, indx, playable, board, players)
            score = word_obj.calculate_word_score(False)
            scored.append({'word': word_obj, 'score': score})
        indx += 1
    return sorted(scored, key=lambda k: k['score'], reverse=True)

# Given a players rack and the board find the highest scoring valid 
# word to play and return information needed to play
def word_rank(rack, board, round_number, players):
    mod_rack = rack.split(", ").copy()
    mod_rack = [x.lower() for x in mod_rack]
    playable = word_position(board)
    scored = get_top_words(playable, board, mod_rack, players)
    check = False
    word_indx = -1
    while check != True:
        word_indx += 1
        check = scored[word_indx]['word'].check_word(round_number, players)
    return scored[word_indx]['word']