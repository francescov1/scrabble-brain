from itertools import combinations
from bisect import bisect_left

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}


def loadvars():
    f = open('anadict.txt', 'r')
    anadict = f.read().split('\n')
    f.close()
    return anadict


def score_word(word):
    return sum([scores[c] for c in word])


def findwords(rack, anadict):
    rack = ''.join(sorted(rack))
    foundwords = []
    for i in range(2, len(rack)+1):
        for comb in combinations(rack, i):
            ana = ''.join(comb)
            j = bisect_left(anadict, ana)
            if j == len(anadict):
                continue
            words = anadict[j].split()
            if words[0] == ana:
                foundwords.extend(words[1:])
    return foundwords


def word_rank(rack, board):
    rack = "akglfer"
    anadict = loadvars()
    foundwords = set(findwords(rack, anadict))
    scored = [(score_word(word), word) for word in foundwords]
    scored.sort()
    for score, word in scored:
        print("%d\t%s" % (score, word))
