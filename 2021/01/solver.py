with open('input') as f:
    i = 0
    slide_window = [int(f.readline()) for x in range(3)]
    print(slide_window)
    for line in f:
        next_window = slide_window[1:] + [int(line.strip())]
        if sum(next_window) > sum(slide_window):
            i += 1
        slide_window = next_window
    print(i)
