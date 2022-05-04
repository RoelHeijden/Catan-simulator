from Color import Color


class IO:

    def __init__(self, game):
        self.c = Color()
        self.game = game

    def select_settlement(self, positions, player):
        print(self.c.color(player.color, player.color))
        print("select settlement position")

        position = ""
        valid = False
        while not valid:
            position = input()
            if not position.isnumeric():
                print("invalid input - enter a number")
            elif int(position) not in positions:
                print("invalid input - settlement location not available")
            else:
                valid = True
        return int(position)

    def select_road(self, edges, player):
        print(self.c.color(player.color, player.color))
        print("select road")
        for i in range(len(edges)):
            road = edges[i].direction[0]
            print("["+str(i+1)+"]", road, edges[i].pos)

        option = ""
        valid = False
        while not valid:
            option = input()
            if not option.isnumeric():
                print("invalid input - enter a number")
            elif int(option) > len(edges) or int(option) <= 0:
                print("invalid input - select on of the options")
            else:
                valid = True
        return edges[int(option)-1]

    def pick_move(self, moves):
        return moves

