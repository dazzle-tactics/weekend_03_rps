from models.player import Player

import random

class Game:
    def __init__(self, move_id_1, move_id_2, winner):
        self.move_id_1 = move_id_1
        self.move_id_2 = move_id_2
        self.winner = winner

# player_1 = Player(1, "rock")
# player_2 = Player(2, "scissors")
# game_1 = Game(0, 0, 0)

# print(player_1.move)
# print(player_2.move)

def convert_move_player_1(player, game):
    if player.move == "rock":
        game.move_id_1 = 1
    elif player.move == "paper":
        game.move_id_1 = 2
    elif player.move == "scissors":
        game.move_id_1 = 3
    print(game.move_id_1)

def convert_move_player_2(player, game):
    if player.move == "rock":
        game.move_id_2 = 1
    elif player.move == "paper":
        game.move_id_2 = 2
    elif player.move == "scissors":
        game.move_id_2 = 3
    print(game.move_id_2)

def move_calc(move_1, move_2, winner):
    if (move_1 - move_2) == -2 or (move_1 - move_2) == 1:
        winner = "Player 1"
   
    elif (move_1 - move_2) == -1 or (move_1 - move_2) == 2:
        winner = "Player 2"

    elif (move_1 - move_2) == 0:
        winner = None
    return winner

def winning_move(result, move_1, move_2):
    if result == "Player 1":
        return move_1
    elif result == "Player 2":
        return move_2

# convert_move_player_1(player_1, game_1)
# convert_move_player_2(player_2, game_1)

# move_calc(game_1.move_id_1, game_1.move_id_2, game_1.winner)
# # move_calc(1, 2, game_1.winner)


def computer_move():
    comp_move = random.randint(0,2)
    computer = Player("Computer", comp_move)
