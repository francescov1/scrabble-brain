import scrabble as scrabble

# player_name = input("Enter your name: ")
# print(player_name)
game = scrabble.Game("Bessie")
game.print_game()

while(not game.is_ended()):

    game.bot_turn(0) 
    game.print_game()

    game.bot_turn(1) 

    game.print_game()

game.end_game()
