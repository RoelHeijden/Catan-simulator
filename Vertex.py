from Color import Color


class Vertex:

    def __init__(self, pos, edges, board):
        self.pos = pos
        self.edges = edges
        self.board = board
        self.player = None
        self.settlement = False
        self.city = False


    def buildable(self):
        buildable = True
        for edge in self.edges:
            for pos in edge.pos:
                if self.board.vertices.get(pos).settlement:
                    buildable = False
        return buildable

    def __str__(self):
        c = Color()

        if self.city:
            return c.background_color("   ", self.player.color)
        if self.settlement:
            return " " + c.background_color(" ", self.player.color) + " "

        if not self.board.show_pos:
            return "   "

        pos = c.color(str(self.pos), "dark gray")
        if self.pos < 10:
            return " " + pos + " "

        if self.pos % 12 >= 6 or self.pos >= 42:
            if self.pos % 2 == 0:
                return pos + " "
            else:
                return " " + pos
        else:
            if self.pos % 2 == 1:
                return pos + " "
            else:
                return " " + pos
