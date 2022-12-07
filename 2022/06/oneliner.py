# fmt: off
print([len({*next(open("i"))[i-4:i]}) for i in range(4095)].index(4))
