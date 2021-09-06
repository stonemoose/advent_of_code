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
        return f'{self.label} -> {self.clockwise.label}'


with open('input') as f:
    cups = [Cup(label) for label in f.read().strip()]
    cups += [Cup(i) for i in range(len(cups)+1, 1000001)]  # Part 2
    num_cups = len(cups)
for cup1, cup2 in zip(cups, cups[1:]+[cups[0]]):
    cup1.clockwise = cup2
current = cups[0]

cups.sort(key=lambda c: c.label)
for cup1, cup2 in zip(cups[1:]+[cups[0]], cups):
    cup1.destination = cup2

for i in range(10000000):  # Change number for part 1
    pickup = current.move()
    current = current.clockwise

current = cups[0].clockwise
print(current.label * current.clockwise.label)
# Part 1
# while(current != cups[0]):
#     print(current.label, end='')
#     current = current.clockwise
# print()
