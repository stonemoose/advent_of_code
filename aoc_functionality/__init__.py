import importlib


def solve(year, day, data):
    mod_name = f"{year}.{day:02}.solver"
    mod = importlib.import_module(mod_name)
    return mod.solve(data)
