from typing import Tuple

"""
Null Heuristic
Always return 0

Complete: Yes
Optimal: Yes
Admissible: Yes
Efficient: No
"""
null_heuristic = lambda values: 0

"""
Misplaced Tile Heuristic
Return number of misplaced tiles on a board.

Complete: Yes
Optimal: Yes
Admissible: Yes
Efficient: Yes
"""
def misplaced(values: Tuple) -> int:
    wrong = 0
    for i, value in enumerate(values):
        if value == 0: continue # Ignore 0 (empty)
        if i + 1 != value:
            # A different number was in expected position.
            wrong += 1
    return wrong

# Map index to correct (row, column) coordinate
correctPlace = [((value - 1) // 3, (value - 1) % 3) for value in range(9)]

"""
Manhattan Distance Heuristic
Return total graphical distance for every number's current to correct position.

Complete: Yes
Optimal: Yes
Admissible: Yes
Efficient: Yes. Most efficient out of the 3.
"""
def manhattan(values: Tuple) -> int:
    total = 0
    for i, value in enumerate(values):
        if value == 0: continue
        # Current row and column of the number
        row, column = i // 3, i % 3
        # Expected row and column of the number
        correctRow, correctColumn = correctPlace[value] #(value - 1) // 3, (value - 1) % 3
        # Difference = difference in x + difference in y
        total += abs(correctRow - row) + abs(correctColumn - column)
    return total
