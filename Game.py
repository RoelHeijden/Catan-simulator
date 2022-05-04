from Player import Player
from Board import Board
from IO import IO
import random


def main():
    game = Game()
    game.play()



"""
to do:
-undo_move()
-validate_moves()
-resource cards for players
-cost for moves
-VP system
"""


class Game:

    def __init__(self):
        self.board = Board(show_pos=True)
        self.backup_board = None
        self.IO = IO(self)
        self.players = [Player(0, "red", self.board),
                        Player(1, "white", self.board),
                        Player(2, "blue", self.board),
                        Player(3, "yellow", self.board)]

    def play(self):
        self.starting_placements()
        # turns = 0
        # while(self.no_winner()):
        #     player = self.players[turns%4]
        #     player.validate_moves()
        #     player.play_dev()
        #     self.roll_dice()
        #     while(!end_turn())
        #         player.get_action()
        #     turns += 1

    def starting_placements(self):
        self.board.show_board()
        for player in self.players:
            settlement = self.start_settlement(player)
            self.start_road(player, settlement)

        for player in reversed(self.players):
            settlement = self.start_settlement(player)
            self.start_road(player, settlement)
            player.init_moves()

    def start_settlement(self, player):
        open_spots = [v.pos for v in self.board.vertex_list if v.buildable()]
        pos = self.IO.select_settlement(open_spots, player)
        v = self.board.vertices.get(pos)
        v.player = player
        v.settlement = True
        self.board.show_board()
        return v

    def start_road(self, player, v):
        road_spots = [edge for edge in v.edges]
        edge = self.IO.select_road(road_spots, player)
        edge.player = player
        edge.road = True
        for pos in edge.pos:
            player.positions[pos] = pos
        self.board.show_board()


main()
