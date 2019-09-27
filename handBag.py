import random as rd 
import <wherever letters initialization is>

def get_new_bag():
    #get full list of letters from LETTERS

    return list(file.LETTERS)

def generate_hand(hand, bag): 
    #For inputs hand and bag, generate hand from the bag up to 7
    random.shuffle(bag) #shuffle bag

    letters_needed = 7 - len(hand)

    hand = hand + "".join(bag[:letters_needed]) #Fill up hand

    #remove letters drawn from bag

    del bag[:letters_needed]

    print("New Hand: %s" , bag)

    return hand
