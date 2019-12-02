import scrabble as scrabble
def get_mv_board(sc_board, mv_board):
    for row in range(0, 15):
        for col in range(0, 15):
            if mv_board[row][col].isalpha():
                sc_board[row][col] = ' ' + mv_board[row][col] + ' '
    return sc_board

def main(mv_board):
    board = scrabble.Board()
    board.board = get_mv_board(board.board, mv_board)
    rack_str = input("input rack: ")
    rack_arr = [char.upper() for char in rack_str]
    rack = scrabble.Rack(rack_arr)
    game = scrabble.Game("bessie", rack, board)
    moves = game.bot_turn(0, rack) 
    print(moves)
    game.print_game()
