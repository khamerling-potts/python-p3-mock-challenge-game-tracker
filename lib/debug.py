#!/usr/bin/env python3
import ipdb

from classes.many_to_many import Player
from classes.many_to_many import Game
from classes.many_to_many import Result

if __name__ == "__main__":
    print("HELLO! :) let's debug :vibing_potato:")

    game1 = Game("blockus")
    game2 = Game("sorry")
    game3 = Game("scrabble")
    player1 = Player("sammy")
    player2 = Player("bob")
    result1 = Result(player1, game1, 10)
    result2 = Result(player2, game2, 15)
    result3 = Result(player1, game3, 20)
    result4 = Result(player1, game1, 110)
    result5 = Result(player2, game1, 50)
    ipdb.set_trace()
