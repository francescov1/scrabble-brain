from itertools import combinations
from bisect import bisect_left
from word_position import word_position

SCORES = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def load_vars():
    f = open('anadict.txt', 'r')
    ana_dict = f.read().split('\n')
    f.close()
    return ana_dict


def score_word(word):
    return sum([SCORES[c] for c in word])


def find_words(rack, ana_dict):
    rack = ''.join(sorted(rack))
    found_words = []
    for i in range(2, len(rack)+1):
        for comb in combinations(rack, i):
            ana = ''.join(comb)
            j = bisect_left(ana_dict, ana)
            if j == len(ana_dict):
                continue
            words = ana_dict[j].split()
            if words[0] == ana:
                found_words.extend(words[1:])
    return found_words


def word_rank(rack, board):
    #board = [['TWS', '   ', '   ', 'DLS', '   ', '   ', '   ', 'TWS', '   ', '   ', '   ', 'DLS', '   ', '   ', 'TWS'], ['   ', 'DWS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'DWS', '   '], ['   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   '], ['DLS', '   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   ', 'DLS'], ['   ', '   ', '   ', '   ', 'DWS', '   ', '   ', '   ', '   ', '   ', 'DWS', '   ', '   ', '   ', '   '], ['   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   '], ['   ', '   ', 'DLS', '   ', '   ', '   ', 'DLS', '   ', 'DLS', '   ', '   ', '   ', 'DLS', '   ', '   '], ['TWS', '   ', '   ', 'DLS', '   ', '   ', '   ', ' R ', ' O ', ' A ', ' D ', 'DLS', '   ', '   ', 'TWS'], ['   ', '   ', 'DLS', '   ', '   ', '   ', ' W ', ' A ', ' T ', ' T ', '   ', '   ', 'DLS', '   ', '   '], ['   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', ' R ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   '], ['   ', '   ', '   ', '   ', ' J ', ' O ', ' K ', ' E ', '   ', '   ', 'DWS', '   ', '   ', '   ', '   '], ['DLS', '   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   ', 'DLS'], ['   ', '   ', 'DWS', '   ', '   ', '   ', 'DLS', '   ', 'DLS', '   ', '   ', '   ', 'DWS', '   ', '   '], ['   ', 'DWS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'TLS', '   ', '   ', '   ', 'DWS', '   '], ['TWS', '   ', '   ', 'DLS', '   ', '   ', '   ', 'TWS', '   ', '   ', '   ', 'DLS', '   ', '   ', 'TWS']]
    rack = rack.split(", ")
    word_position(board)



    # ana_dict = load_vars()
    # found_words = set(find_words(rack, ana_dict))
    # scored = [(score_word(word), word) for word in found_words]
    # scored.sort()
    # for score, word in scored:
    #     print("%d\t%s" % (score, word))
