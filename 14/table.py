import random

names = ["Julian", "Bob", "PyBites", "Dante", "Martin", "Rodolfo"]
aliases = ["Pythonista", "Nerd", "Coder"] * 2
points = random.sample(range(81, 101), 6)
awake = [True, False] * 3
SEPARATOR = " | "


def generate_table(*args):
    for item in zip(*args):
        yield SEPARATOR.join(map(str, item))
