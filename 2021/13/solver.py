import numpy as np


def fold_paper(paper, dim):
    num = paper.shape[dim == "x"] // 2
    if dim == "y":
        return np.logical_or(paper[:num], paper[:num:-1])
    if dim == "x":
        return np.logical_or(paper[:, :num], paper[:, :num:-1])


with open("input") as f:
    coords, fold_strings = f.read().strip().split("\n\n")
    coordinates = [list(map(int, c.split(","))) for c in coords.split("\n")]
    folds = [fold.split("=")[0][-1] for fold in fold_strings.split("\n")]


x_len = max([coord[0] for coord in coordinates]) + 1
y_len = max([coord[1] for coord in coordinates]) + 1
paper = np.full((y_len, x_len), False)

for x, y in coordinates:
    paper[y, x] = True

paper = fold_paper(paper, folds[0])
print("Part 1: ", np.sum(paper))

for dim in folds[1:]:
    paper = fold_paper(paper, dim)

print("Part 2:")
for line in paper:
    print("".join(["█" if x else " " for x in line]))
