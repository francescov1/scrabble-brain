import scrabble as scrabble

def get_player_input():
    word_to_play = input("Word to play: ")
    col = input("Column number: ")
    row = input("Row number: ")
    direction = input("Direction of word (r - right or d - down): ")
    print("\n================================================================================================\n")

    return (word_to_play, int(col), int(row), direction)

player_name = input("Enter your name: ")
print(player_name)
game = scrabble.Game(player_name)
game.print_game()

while(not game.is_ended()):

    (word_to_play, col, row, direction) = get_player_input()
    game.player_turn(word_to_play, row, col, direction)
    game.print_game()

    game.bot_turn(1) 

    game.print_game()

game.end_game()
