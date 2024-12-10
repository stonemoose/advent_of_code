class Cup:
    def __init__(self, label):
        self.label = int(label)
        self.clockwise = None
        self.destination = None

    def get_destination(self, pickup):
        destination = self.destination
        if destination in pickup:
            return destination.get_destination(pickup)
        return destination

    def move(self):
        a = self.clockwise
        b = a.clockwise
        c = b.clockwise
        self.clockwise = c.clockwise

        dest = self.get_destination((a, b, c))
        dest.clockwise, c.clockwise = a, dest.clockwise

    def __str__(self, start=None):
        return f"{self.label} -> {self.clockwise.label}"


def crab_cups(cups, moves=100):
    for cup1, cup2 in zip(cups, cups[1:] + [cups[0]]):
        cup1.clockwise = cup2
    current = cups[0]

    cups.sort(key=lambda c: c.label)
    for cup1, cup2 in zip(cups[1:] + [cups[0]], cups):
        cup1.destination = cup2

    for _ in range(moves):
        current.move()
        current = current.clockwise
    return cups


def solve(input_data):
    cups = [Cup(label) for label in input_data]
    million_cups = [Cup(label) for label in input_data]
    million_cups += [Cup(i) for i in range(len(million_cups) + 1, 1000001)]

    cups = crab_cups(cups)
    current = cups[0].clockwise
    p1 = ""
    while current != cups[0]:
        p1 += str(current.label)
        current = current.clockwise

    million_cups = crab_cups(million_cups, 10_000_000)
    cup_one = million_cups[0].clockwise
    p2 = cup_one.label * cup_one.clockwise.label
    return p1, p2
