

class Move:

    def __init__(self, ID, action, location):
        self.ID = ID
        self.action = action
        self.location = location
        self.cost = self.get_cost()

    def get_cost(self):
        switcher = {
            "road": 0,
            "settlement": 0,
            "city": 0,
        }
        return switcher.get(self.action)

    def play(self, player):
        a = self.action

        if a == "road":
            self.build_road(player)

        if a == "settlement":
            self.build_settlement(player)

        if a == "city":
            self.build_city(player)

    def build_road(self, player):
        road = self.location
        road.road = True
        road.player = player
        player.roads_left -= 1

        for pos in road.pos:
            if not player.positions.get(pos):
                player.positions[pos] = pos
                v = player.board.vertices.get(pos)

                for edge in v.edges:
                    if edge.pos != road.pos:
                        player.add_move("road", edge)

                if v.buildable():
                    player.add_move("settlement", v)

    def build_settlement(self, player):
        settlement = self.location
        settlement.settlement = True
        settlement.player = player
        player.settlements_left -= 1

        player.add_move("city", settlement)

        for edge in settlement.edges:
            for pos in edge.pos:
                if pos != settlement.pos:
                    if player.positions.get(pos):

                        moves = player.moves.get("settlement")
                        to_remove = []
                        for k in moves:
                            move = moves.get(k)
                            if move.location.pos == pos:
                                to_remove.append(move.ID)
                        for ID in to_remove:
                            moves.pop(ID)

    def build_city(self, player):
        city = self.location
        city.city = True
        player.cities_left -= 1
        player.settlements_left += 1


    def __str__(self):
        return str(self.ID) + " " + self.action + " " + str(self.location.pos)
