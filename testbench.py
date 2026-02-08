from board import Board

print("Testbench")

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
  

def testBoard(b: Board, manhattan_ans: int, misplaced_ans: int, solution_ans: bool = False) -> None:
    b.printBoard()
    print(f"isSolution() function: {'Passed' if b.isSolution() == solution_ans else 'Failed'}")
    print(f"Manhattan Distance Test: {'Passed' if manhattan(b) == manhattan_ans else 'Failed'}")
    print(f"Misplaced Tile Test: {'Passed' if misplaced(b) == misplaced_ans else 'Failed'}")

perfect = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
perfectBoard = Board(perfect)

print("Test 1 (Perfect Board)")
testBoard(perfectBoard, 0, 0, True)
