from flask import render_template
from rps import app
from models.game import *
from models.player import *

@app.route('/')
def index():
    return render_template('index.html', title="Ro Sham Bo")

@app.route('/<move_1>/<move_2>')
def rps(move_1, move_2):
    player_1 = Player("Player 1", move_1)
    player_2 = Player("Player 2", move_2)
    game_1 = Game(0, 0, "none yet")
    convert_move_player_1(player_1, game_1)
    convert_move_player_2(player_2, game_1)
    result = move_calc(game_1.move_id_1, game_1.move_id_2, game_1.winner)
    win_move = winning_move(result, move_1, move_2)
    return render_template('winner.html', title="RPS", result=result, win_move=win_move, move_1 = move_1, move_2 = move_2, player_1=player_1.name, player_2=player_2.name)

@app.route('/<move_1>/computer')
def computer(move_1):
    player_1 = Player("Player 1", move_1)
    comp_move = random.randint(0,2)
    computer = Player("Computer", comp_move)
    game_1 = Game(0, 0, "none yet")
    convert_move_player_1(player_1, game_1)
    result = move_calc(game_1.move_id_1, game_1.move_id_2, game_1.winner)
    win_move = winning_move(result, move_1, comp_move)
    return render_template('winner.html', title="Ro Sham Bo", result=result, win_move=win_move, move_1 = move_1, comp_move = comp_move, player_1=player_1.name)