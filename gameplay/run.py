import scrabble as scrabble

# add function to format the input board
board = scrabble.Board()

rack_str = input("input rack: ")
rack_arr = [char.upper() for char in rack_str]
rack = scrabble.Rack(rack_arr)
game = scrabble.Game("bessie", rack, board)

game.bot_turn(0, rack) 

game.print_game()
