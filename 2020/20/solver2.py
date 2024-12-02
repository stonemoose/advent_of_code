class Tile:
    def __init__(self, tile):
        self.id = int(tile[0][5:9])
        self.image = [line for line in tile[1:]]
        self.top = self.bot = self.right = self.left = None
        self.top_edge = self.image[0]
        self.bot_edge = self.image[-1][::-1]
        self.right_edge = "".join([line[-1] for line in self.image])
        self.left_edge = "".join([line[0] for line in self.image])[::-1]
        self.flipped = False
        self.direction = 0
        self.edges = set(
            [
                self.top_edge,  # 0
                self.right_edge,  # 1
                self.bot_edge,  # 2
                self.left_edge,  # 3
            ]
        )
        self.mirror_edges = set(e[::-1] for e in self.edges)
        self.neighbours = 0

    def match(self, other):
        if self.edges.intersection(other.edges) or self.edges.intersection(
            other.mirror_edges
        ):
            self.neighbours += 1
            other.neighbours += 1


with open("input") as f:
    bit_file = f.read().replace("#", "1").replace(".", "0")
    tiles = [Tile(tile.split("\n")) for tile in bit_file.strip().split("\n\n")]

for i, tile1 in enumerate(tiles[:-1]):
    for tile2 in tiles[i + 1 :]:
        tile1.match(tile2)

ans = 1
for tile in tiles:
    if tile.neighbours == 2:
        ans *= tile.id
        print(tile.id)
print(ans)
