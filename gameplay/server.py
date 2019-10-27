import scrabble as scrabble
from flask import Flask, request, jsonify
app = Flask(__name__)

debug_gameplay = True
game = None

# TODO: need to send back info about each turn (ie current score, if turn was
# skipped or not, updated board)

@app.route('/start', methods=['POST'])
def start_game():
    data = request.get_json()
    player_name = data['player_name']
    this.game = scrabble.Game(player_name)

    if (debug_gameplay):
        this.game.print_game()

    return jsonify({ "board": this.game.get_board_data() })

# performs a player turn and a bot turn
# TODO: instead of a start route, simply start game from round route if
# no game currently exists
# - if there is no game variable and the move made by the player is not
# the first move, show an error (game state deleted from brain memory) 
@app.route('/round', methods=['POST'])
def game_round():
    data = request.get_json()

    this.game.player_turn(
        data['word_played'],
        data['col'],
        data['row'],
        data['direction']
    )

    if (debug_gameplay):
        this.game.print_game()

    # TODO: return winner in end_game, dont need string or anything
    if (this.game.is_ended()):
        return jsonify({
            "board": this.game.get_board_data(),
            "result": this.game.end_game()
        })

    this.game.bot_turn()

    if (debug_gameplay):
        this.game.print_game()

    if (this.game.is_ended()):
        return jsonify({
            "board": this.game.get_board_data(),
            "result": this.game.end_game()
        })

    return jsonify({ "board": this.game.get_board_data() })

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)
