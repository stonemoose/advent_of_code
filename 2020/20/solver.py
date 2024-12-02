class Tile:

    def __init__(self, tile):
        self.id = int(tile[0][5:9])
        self.image = [line for line in tile[1:]]
        self.top = self.bot = self.right = self.left = None
        self.top_edge = self.image[0]
        self.bot_edge = self.image[-1][::-1]
        self.right_edge = "".join([line[-1] for line in self.image])
        self.left_edge = "".join([line[0] for line in self.image])[::-1]
        # self.image = [line[1:-1] for line in self.image[1:-1]]
        self.flipped = False
        self.direction = 0
        self.edges = [
            self.top_edge,  # 0
            self.right_edge,  # 1
            self.bot_edge,  # 2
            self.left_edge,  # 3
        ]
        self.mirror_edges = set(e[::-1] for e in self.edges)
        self.neighbours = [None, None, None, None]

    def match(self, other):
        for i in range(4):
            edge = self.edges[i]
            if edge in other.edges:
                self.neighbours[i] = other
                other.flip(self.flipped)
                other.set_dir(edge, (i + 2) % 4)
                break
            elif edge[::-1] in other.edges:
                self.neighbours[i] = other
                other.flip(self.flipped)
                other.set_dir(edge, (i + 2) % 4)
                break

    def flip(self, from_flipped):
        if not (from_flipped or self.flipped):
            self.flipped = True
            self.edges = {e[::-1] for e in self.edges}
            self.edges[0], self.edges[2] = self.edges[2], self.edges[0]

    def set_dir(self, edge, direction):
        self.direction = (self.edges.index(edge) - direction) % 4

    def turn(self, edge, direction):
        self.direction = (self.edges.index(edge) - direction) % 4

    def num_neighbours(self):
        return sum(bool(n) for n in self.neighbours)


with open("test") as f:
    bit_file = f.read().replace("#", "1").replace(".", "0")
    tiles = [Tile(tile.split("\n")) for tile in bit_file.strip().split("\n\n")]


# for i, tile in enumerate(tiles):
#     if tile.all_neighbours():
#         for other_tile in tiles[i:]:
#             tile.match(other_tile)

for line in tiles[0].image:
    print(line)
