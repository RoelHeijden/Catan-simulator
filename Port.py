from Color import Color


class Port:

    def __init__(self, pos, type):
        self.pos = pos
        self.type = type
        self.vertices = []

    def __str__(self):
        c = Color()
        t = c.color("2:1", "white")

        switcher = {
            "2:1 sheep": t + c.color(" sheep", "sheep"),
            "2:1 wood": t + c.color(" wood ", "wood"),
            "2:1 ore": t + c.color(" ore  ", "ore"),
            "2:1 wheat": t + c.color(" wheat", "wheat"),
            "2:1 brick": t + c.color(" brick", "brick"),
            "3:1": c.color("3:1      ", "white"),
        }

        if self.type == "3:1":
            if self.pos == 0 or self.pos == 4:
                return c.color("  3:1    ", "white")
            if self.pos == 5:
                return c.color("   3:1   ", "white")
            if self.pos == 6 or self.pos == 7 or self.pos == 8:
                return c.color("      3:1", "white")

        if self.type == "2:1 ore":
            if self.pos == 0 or self.pos == 5:
                return " " + t + c.color(" ore ", "ore")
            if self.pos == 6 or self.pos == 7 or self.pos == 8:
                return "  " + t + c.color(" ore", "ore")

        if self.type == "2:1 wood":
            if self.pos == 6 or self.pos == 7 or self.pos == 8:
                return " " + t + c.color(" wood", "wood")

        return switcher.get(self.type)

    def get_vertex_nums(self):
        switcher = {
            0: (0, 1),
            1: (5, 10),
            2: (23, 29),
            3: (41, 47),
            4: (50, 51),
            5: (48, 49),
            6: (36, 42),
            7: (18, 24),
            8: (2, 7),
        }
        return switcher.get(self.pos)
