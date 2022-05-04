from Color import Color


class Tile:

    def __init__(self, pos):
        self.pos = pos
        self.neighbours = self.get_neighbours()
        self.vertices = self.get_vertex_nums()
        self.blocked = False
        self.vertices = []
        self.resource = ""
        self.number = 0

    def get_neighbours(self):
        switcher = {
            0: [1, 2, 4],
            1: [0, 3, 6, 4],
            2: [0, 4, 7, 5],
            3: [1, 6, 8],
            4: [0, 1, 2, 6, 7, 9],
            5: [2, 7, 10],
            6: [1, 3, 4, 8, 11, 9],
            7: [2, 4, 5, 9, 10, 12],
            8: [3, 6, 11, 13],
            9: [4, 6, 7, 11, 14, 12],
            10: [5, 7, 12, 15],
            11: [6, 8, 9, 13, 14, 16],
            12: [7, 9, 10, 14, 17, 15],
            13: [8, 11, 16],
            14: [9, 11, 12, 16, 18, 17],
            15: [10, 12, 17],
            16: [11, 13, 14, 18],
            17: [12, 14, 15, 18],
            18: [14, 16, 17]
        }
        return switcher.get(self.pos)

    def get_vertex_nums(self):
        switcher = {
            0: [1, 2, 3, 4, 8, 9],
            1: [2, 3, 7, 8, 13, 14],
            2: [4, 5, 9, 10, 15, 16],
            3: [6, 7, 12, 13, 18, 19],
            4: [8, 9, 14, 15, 20, 21],
            5: [10, 11, 16, 17, 22, 23],
            6: [13, 14, 19, 20, 25, 26],
            7: [15, 16, 21, 22, 27, 28],
            8: [18, 19, 24, 25, 30, 31],
            9: [20, 21, 26, 27, 32, 33],
            10: [22, 23, 28, 29, 34, 35],
            11: [25, 26, 31, 32, 37, 38],
            12: [27, 28, 33, 34, 39, 40],
            13: [30, 31, 36, 37, 42, 43],
            14: [32, 33, 38, 39, 44, 45],
            15: [34, 35, 40, 41, 46, 47],
            16: [37, 38, 43, 44, 48, 49],
            17: [39, 40, 45, 46, 50, 51],
            18: [44, 45, 49, 50, 52, 53],
        }
        return switcher.get(self.pos)

    def __str__(self):
        c = Color()
        if self.resource is None or self.number is None:
            if self.blocked:
                return "  " + c.blocked("    ", "sheep") + "  "
            else:
                return "        "

        colored = {
            "brick": c.color(" brick", "brick"),
            "ore": c.color(" ore", "ore") + " ",
            "wood": c.color(" wood", "wood") + " ",
            "wheat": c.color(" wheat", "wheat"),
            "sheep": c.color(" sheep", "sheep"),
            "brick blocked": c.blocked(" brick", "brick"),
            "ore blocked": c.blocked(" ore", "ore") + " ",
            "wood blocked": c.blocked(" wood", "wood") + " ",
            "wheat blocked": c.blocked(" wheat", "wheat"),
            "sheep blocked": c.blocked(" sheep", "sheep")
        }

        n = str(self.number)
        r = colored.get(self.resource)

        if self.number == 6 or self.number == 8:
            n = '\033[1;91m' + n + '\033[0m'
        else:
            n = '\033[1;30m' + n + '\033[0m'

        if self.blocked:
            n = c.background_color(n, "black", True)
        if self.blocked:
            r = colored.get(self.resource + " blocked")

        if self.number <= 9:
            n = " " + n

        if self.resource == "ore":
            if self.number <= 9:
                r = r + " "
            else:
                n = " " + n

        return n + r


