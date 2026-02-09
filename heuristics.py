from board import Board

def misplaced(b: Board) -> int:
    total = 0
    for i, (_, _, value) in enumerate(b.getBoardData()):
        if value == 0: continue # Ignore 0 (empty)
        if i + 1 != value:
            total += 1
    return total

def manhattan(b: Board) -> int:
    total = 0
    for row, column, value in b.getBoardData():
        if value == 0: continue
        correctRow, correctColumn = (value - 1) // 3, (value - 1) % 3
        total += abs(correctRow - row) + abs(correctColumn - column)
    return total