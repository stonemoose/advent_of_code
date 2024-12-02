import numpy as np


def enhance(input_img, enhance_alg, iteration=0):

    def calculate_number(x, y, input_img):
        out = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                out = out * 2 + input_img[x + i, y + j]
        return out

    input_img = np.pad(input_img, 2, constant_values=iteration % 2)
    out_img = np.zeros([s - 2 for s in input_img.shape], int)
    for x in range(len(out_img)):
        for y in range(len(out_img)):
            out_img[x, y] = enhance_alg[calculate_number(x + 1, y + 1, input_img)]
    return out_img


with open("input") as f:
    alg, img = f.read().split("\n\n")
    enhancement_alg = [int(char == "#") for char in alg]
    input_image = [[int(c == "#") for c in line] for line in img.strip().split("\n")]
    input_image = np.array(input_image)


for i in range(50):
    input_image = enhance(input_image, enhancement_alg, i)

print(sum(sum(x) for x in input_image))
