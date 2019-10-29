import scrabble as scrabble
from flask import Flask, request, jsonify
app = Flask(__name__)

debug_gameplay = True
game = None

# get game results and remove game from memory
def end_game():
    board = this.game.get_board_data()
    result = this.game.end_game()
    this.game = None
    return jsonify({
        "board": board,
        "result": result
    })

# ensure that if no game exists, the board only contains one word
def verify_new_game(board_arr):
    # TODO: check if there is one one word in board_arr
    return True # or False

# TODO: need to send back info about each turn (ie current score, if turn was
# skipped or not, updated board)

# performs a player turn and a bot turn
@app.route('/round', methods=['POST'])
def game_round():
    data = request.get_json()
    board_arr = data['board']

    if (this.game is None):
        if (verify_new_game(board_arr)):
            # dont think theres much use to take the player's name?
            player_name = "player"
            this.game = scrabble.Game(player_name)

            if (debug_gameplay):
                this.game.print_game()
        else:
            err = "Game state not found in brain"
            print(err)
            return jsonify({ "error": err })

    # may be able to combine these two, may be faster than picking out
    # word then making player turn
    (word_played, col, row, direction) = this.game.get_word_played(board_arr)
    this.game.player_turn(word_played, col, row, direction)

    if (debug_gameplay):
        this.game.print_game()

    # TODO: return winner in end_game, dont need string or anything
    if (this.game.is_ended()):
        return end_game();

    this.game.bot_turn()

    if (debug_gameplay):
        this.game.print_game()

    if (this.game.is_ended()):
        return end_game();

    return jsonify({ "board": this.game.get_board_data() })

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)