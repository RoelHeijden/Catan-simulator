from Color import Color


class Edge:

    def __init__(self, v1, v2):
        self.pos = (v1, v2)
        self.road = False
        self.player = None
        self.direction = self.get_direction()

    def get_direction(self):
        v1 = self.pos[0]
        v2 = self.pos[1]

        if abs(v2 - v1) == 1:
            return "- -  - -"

        if abs(v2 - v1) == 3 or v2 - v1 == 5:
            if v1 % 2 == 0:
                return "/"
            else:
                return "\\"

        if abs(v2 - v1) == 6:
            if v1 % 2 == 0:
                if v1 % 12 < 6:
                    return "\\"
                else:
                    return "/"
            else:
                if v1 % 12 < 6:
                    return "/"
                else:
                    return "\\"

    def __str__(self):
        c = Color()
        if self.player is None:
            return c.color(self.direction, "dark gray")
        else:
            return c.color(self.direction, self.player.color)





