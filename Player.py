from Move import Move

"""
-place road       (edge)          = add moves(roads, settlements), remove moves(self)
-place settlement (vertex)        = add moves(city),               remove moves(self) remove moves(neighbours)
-place city       (vertex)        = None,                          remove moves(self)

-buy dev card     ()              = add moves(play dev card),      remove moves(self)
-play dev card    (dev card)      =
-trade            (resource card) =
-roll dice        ()              =
"""


class Player:

    def __init__(self, pos, color, board):
        self.board = board
        self.pos = pos
        self.color = color
        self.VP = 0

        self.positions = {}
        self.resources = []
        self.dev_cards = []

        self.roads_left = 15
        self.settlements_left = 5
        self.cities_left = 4

        self.moves = {}
        self.move_id = 0

    def init_moves(self):
        moves = {
            "road": self.road_moves(),
            "settlement": self.settlement_moves(),
            "city": self.city_moves(),
        }
        self.moves = moves

    def road_moves(self):
        moves = {}
        for pos in self.positions:
            for edge in self.board.vertices.get(pos).edges:
                if not edge.road:
                    m = Move(self.move_id, "road", edge)
                    moves[self.move_id] = m
                    self.move_id += 1
        return moves

    def settlement_moves(self):
        moves = {}
        for pos in self.positions:
            v = self.board.vertices.get(pos)
            if v.buildable():
                m = Move(self.move_id, "settlement", self.board.vertices.get(pos))
                moves[self.move_id] = m
                self.move_id += 1
        return moves

    def city_moves(self):
        moves = {}
        for pos in self.positions:
            vertex = self.board.vertices.get(pos)
            if vertex.settlement and not vertex.city:
                m = Move(self.move_id, "city", vertex)
                moves[self.move_id] = m
                self.move_id += 1
        return moves

    def play_move(self, move):
        self.moves.get(move.action).pop(move.ID)
        move.play(self)

    def add_move(self, action, location):
        self.moves.get(action)[self.move_id] = Move(self.move_id, action, location)
        self.move_id += 1

    def show_moves(self):
        for action_type in self.moves:
            moves = self.moves.get(action_type)
            for move in moves:
                print(moves.get(move))
        print()
