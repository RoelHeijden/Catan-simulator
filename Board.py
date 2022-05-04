import random
from Tile import Tile
from Port import Port
from Vertex import Vertex
from Edge import Edge
from Color import Color


"""
Board structure:
- {54 Vertices} = each has 2-3 edges          -> [edge, edge...]
- [72 Edges]    = each has 2 vertex positions -> (pos, pos)
- [19 Tiles]    = each has 6 vertex positions -> [pos, pos...]
- [9 Ports]     = each has 2 vertex positions -> (pos, pos)
"""


class Board:

    def __init__(self, show_pos=False):
        self.show_pos = show_pos
        self.N_OF_TILES = 19
        self.N_OF_VERTICES = 54
        self.numbers = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12]

        self.resources = ["brick", "brick", "brick", "ore", "ore", "ore", "wheat", "wheat", "wheat", "wheat",
                          "wood", "wood", "wood", "wood", "sheep", "sheep", "sheep", "sheep"]
        self.port_types = ["2:1 sheep", "2:1 wood", "2:1 ore", "2:1 wheat", "2:1 brick",
                           "3:1", "3:1", "3:1", "3:1"]

        self.edges = self.init_edges()
        self.vertices = self.init_vertices()
        self.vertex_list = [self.vertices[k] for k in self.vertices.keys()]
        self.tiles = self.init_tiles(self.numbers, self.resources)
        self.ports = self.init_ports(self.port_types)

    # initializes all 72 edges
    # returns list of edges
    def init_edges(self):
        edges = [Edge(0, 1),
                 Edge(0, 3),
                 Edge(1, 4),
                 Edge(2, 3),
                 Edge(4, 5),
                 Edge(2, 7),
                 Edge(3, 8),
                 Edge(4, 9),
                 Edge(5, 10),
                 Edge(6, 7),
                 Edge(8, 9),
                 Edge(10, 11),
                 Edge(6, 12),
                 Edge(7, 13),
                 Edge(8, 14),
                 Edge(9, 15),
                 Edge(10, 16),
                 Edge(11, 17),
                 Edge(13, 14),
                 Edge(15, 16),
                 Edge(12, 18),
                 Edge(13, 19),
                 Edge(14, 20),
                 Edge(15, 21),
                 Edge(16, 22),
                 Edge(17, 23),
                 Edge(18, 19),
                 Edge(20, 21),
                 Edge(22, 23),
                 Edge(18, 24),
                 Edge(19, 25),
                 Edge(20, 26),
                 Edge(21, 27),
                 Edge(22, 28),
                 Edge(23, 29),
                 Edge(25, 26),
                 Edge(27, 28),
                 Edge(24, 30),
                 Edge(25, 31),
                 Edge(26, 32),
                 Edge(27, 33),
                 Edge(28, 34),
                 Edge(29, 35),
                 Edge(30, 31),
                 Edge(32, 33),
                 Edge(34, 35),
                 Edge(30, 36),
                 Edge(31, 37),
                 Edge(32, 38),
                 Edge(33, 39),
                 Edge(34, 40),
                 Edge(35, 41),
                 Edge(37, 38),
                 Edge(39, 40),
                 Edge(36, 42),
                 Edge(37, 43),
                 Edge(38, 44),
                 Edge(39, 45),
                 Edge(40, 46),
                 Edge(41, 47),
                 Edge(42, 43),
                 Edge(44, 45),
                 Edge(46, 47),
                 Edge(43, 48),
                 Edge(44, 49),
                 Edge(45, 50),
                 Edge(46, 51),
                 Edge(48, 49),
                 Edge(50, 51),
                 Edge(49, 52),
                 Edge(50, 53),
                 Edge(52, 53)]
        return edges

    # Initializes all 54 vertices
    # Returns dictionary of vertices
    def init_vertices(self):
        vertices = {}
        for i in range(self.N_OF_VERTICES):
            edges = []
            for edge in self.edges:
                if i in edge.pos:
                    edges.append(edge)
            vertices[i] = (Vertex(i, edges, self))
        return vertices

    # Initializes all 19 tiles
    # Randomized resource and number
    # Returns list of tiles
    def init_tiles(self, numbers, resources):
        tiles = [Tile(i) for i in range(self.N_OF_TILES)]
        terrain = []
        random.shuffle(numbers)

        for r, n in zip(resources, numbers):
            terrain.append((r, n))
        terrain.append((None, None))

        random.shuffle(terrain)
        while not self.valid_numbers(terrain, tiles):
            random.shuffle(terrain)

        for tile, (r, n) in zip(tiles, terrain):
            tile.resource = r
            tile.number = n
            for num in tile.get_vertex_nums():
                tile.vertices.append(self.vertices[num])
            if r is None:
                tile.blocked = True

        return tiles

    # Checks if number/resource configuration is valid
    # Returns Boolean
    def valid_numbers(self, terrain, tiles):
        for tile, (_, n) in zip(tiles, terrain):

            for neighbour in tile.neighbours:
                nn = terrain[neighbour][1]
                if nn == n:
                    return False

            if n == 6:
                for neighbour in tile.neighbours:
                    nn = terrain[neighbour][1]
                    if nn == 8:
                        return False

            if n == 2:
                for neighbour in tile.neighbours:
                    nn = terrain[neighbour][1]
                    if nn == 12:
                        return False
        return True

    # Initializes all 9 ports
    # Randomized port type
    # Returns list of ports
    def init_ports(self, types):
        ports = []
        random.shuffle(types)
        for i in range(len(types)):
            ports.append(Port(i, types[i]))

        for port in ports:
            for num in port.get_vertex_nums():
                port.vertices.append(self.vertices[num])

        return ports


# """
    def show_board(self):
        t = self.tiles
        p = self.ports
        v = self.vertex_list
        e = self.edges
        c = Color()
        port_color = "gray"
        p1 = c.color("- - -", port_color)
        p2 = c.color("\\", port_color)
        p3 = c.color("/", port_color)


        print("                                             ", p[0], "                                         ")
        print("                                               ", p3, "", p2, "                                               ")
        print("                                              ", p3, "  ", p2, "                                              ")
        print("                                           "+str(v[0])+str(e[0])+str(v[1])+"                                          ")
        print("                                          ", e[1], "          ", e[2], "                                          ")
        print("                                         ", e[1], "            ", e[2], "                                         ")
        print("             ", p[8], p1+str(v[2])+str(e[3])+str(v[3])+"  ", t[0], "  "+str(v[4])+str(e[4])+str(v[5])+p1, p[1], "         ")
        print("                       ", p2, "  ", e[5], "          ", e[6], "            ", e[7], "          ", e[8], "  ", p3, "                      ")
        print("                        ", p2, "", e[5], "            ", e[6], "          ", e[7], "            ", e[8], "", p3, "                        ")
        print("               "+str(v[6])+str(e[9])+str(v[7])+"  ", t[1], "  "+str(v[8])+str(e[10])+str(v[9])+"  ", t[2], "  "+str(v[10])+str(e[11])+str(v[11])+"     ")
        print("              ", e[12], "          ", e[13], "            ", e[14], "          ", e[15], "            ", e[16], "          ", e[17], "              ")
        print("             ", e[12], "            ", e[13], "          ", e[14], "            ", e[15], "          ", e[16], "            ", e[17], "             ")
        print("            "+str(v[12])+"  ", t[3], "  "+str(v[13])+str(e[18])+str(v[14])+"  ", t[4], "  "+str(v[15])+str(e[19])+str(v[16])+"  ", t[5], "  "+str(v[17])+"    ")
        print("             ", e[20], "            ", e[21], "          ", e[22], "            ", e[23], "          ", e[24], "            ", e[25], "             ")
        print("              ", e[20], "          ", e[21], "            ", e[22], "          ", e[23], "            ", e[24], "          ", e[25], "              ")
        print(p[7], p1+str(v[18])+str(e[26])+str(v[19])+"  ", t[6], "  "+str(v[20])+str(e[27])+str(v[21])+"  ", t[7], "  "+str(v[22])+str(e[28])+str(v[23])+p1, p[2])
        print("         ", p2, "  ", e[29], "          ", e[30], "            ", e[31], "          ", e[32], "            ", e[33], "          ", e[34], "  ", p3, "          ")
        print("          ", p2, "", e[29], "            ", e[30], "          ", e[31], "            ", e[32], "          ", e[33], "            ", e[34], "", p3, "           ")
        print("            "+str(v[24])+"  ", t[8], "  "+str(v[25])+str(e[35])+str(v[26])+"  ", t[9], "  "+str(v[27])+str(e[36])+str(v[28])+"  ", t[10], "  "+str(v[29])+"   ")
        print("             ", e[37], "            ", e[38], "          ", e[39], "            ", e[40], "          ", e[41], "            ", e[42], "             ")
        print("              ", e[37], "          ", e[38], "            ", e[39], "          ", e[40], "            ", e[41], "          ", e[42], "              ")
        print("               "+str(v[30])+str(e[43])+str(v[31])+"  ", t[11], "  "+str(v[32])+str(e[44])+str(v[33])+"  ", t[12], "  "+str(v[34])+str(e[45])+str(v[35])+"     ")
        print("              ", e[46], "          ", e[47], "            ", e[48], "          ", e[49], "            ", e[50], "          ", e[51], "              ")
        print("             ", e[46], "            ", e[47], "          ", e[48], "            ", e[49], "          ", e[50], "            ", e[51], "             ")
        print("            "+str(v[36])+"  ", t[13], "  "+str(v[37])+str(e[52])+str(v[38])+"  ", t[14], "  "+str(v[39])+str(e[53])+str(v[40])+"  ", t[15], "  "+str(v[41])+"   ")
        print("          ", p3, "", e[54], "            ", e[55], "          ", e[56], "            ", e[57], "          ", e[58], "            ", e[59], "", p2, "           ")
        print("         ", p3, "  ", e[54], "          ", e[55], "            ", e[56], "          ", e[57], "            ", e[58], "          ", e[59], "  ", p2, "           ")
        print(p[6], p1+str(v[42])+str(e[60])+str(v[43])+"  ", t[16], "  "+str(v[44])+str(e[61])+str(v[45])+"  ", t[17], "  "+str(v[46])+str(e[62])+str(v[47])+p1, p[3])
        print("                           ", e[63], "            ", e[64], "          ", e[65], "            ", e[66], "                           ")
        print("                            ", e[63], "          ", e[64], "            ", e[65], "          ", e[66], "                            ")
        print("                             "+str(v[48])+str(e[67])+str(v[49])+"  ", t[18], "  "+str(v[50])+str(e[68])+str(v[51])+"                        ")
        print("                               ", p2, "   ", p3, " ", e[69], "            ", e[70], " ", p2, "   ", p3, "                                ")
        print("                                ", p2, " ", p3, "   ", e[69], "          ", e[70], "   ", p2, " ", p3, "                                  ")
        print("                              ", p[5], "  "+str(v[52])+str(e[71])+str(v[53])+"   ", p[4], "                        ")
        print()
        
# """