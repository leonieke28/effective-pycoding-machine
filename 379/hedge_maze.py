from typing import List, Tuple


DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def hedge_maze(maze: List[List[str]], entrance: Tuple[int, int]) -> int:
    """Finds the shortest distance from the entrance to the nearest exit in a maze."""