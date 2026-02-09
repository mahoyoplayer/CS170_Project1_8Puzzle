from functools import lru_cache

def null_heuristic(values) -> int:
    return 0

@lru_cache(maxsize=None)
def misplaced(values) -> int:
    total = 0
    for i, value in enumerate(values):
        if value == 0: continue # Ignore 0 (empty)
        if i + 1 != value:
            total += 1
    return total

correctPlace = tuple(((value - 1) // 3, (value - 1) % 3) for value in range(9))

@lru_cache(maxsize=None)
def manhattan(values) -> int:
    total = 0
    for i, value in enumerate(values):
        row, column = i // 3, i % 3
        correctRow, correctColumn = correctPlace[value] #(value - 1) // 3, (value - 1) % 3
        total += abs(correctRow - row) + abs(correctColumn - column)
    return total