from flask import render_template, request
from app import app
from app.models.player_list import *
from app.models.game.game import *


@app.route('/<choice1>/<choice2>')
def play_game(choice1, choice2):
    game = Game(players)
    game.players[0].choice = choice1
    game.players[1].choice = choice2
    result = game.play_game()
    return render_template('index.html', title='Game', game=game, result=result)



