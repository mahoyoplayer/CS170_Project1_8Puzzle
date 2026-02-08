from typing import List
import copy

class Board:
    BOARD_SIZE = 3

    def __init__(self, rows: List[List[int]]):
        if len(rows) != self.BOARD_SIZE:
            raise RuntimeError("Board must three rows.")
        elif False in [len(row) == self.BOARD_SIZE for row in rows]:
            raise RuntimeError("Board can only have three values in each row.")
        self.rows = copy.deepcopy(rows)

    def getValue(self, row: int, column: int) -> int:
        return self.rows[row][column]

    def getBoardData(self) -> List[List[int]]:
        res = [0] * 9
        for i in range(9):
            row = i // 3
            column = i % 3
            res[i] = (row, column, self.getValue(row, column))
        return res

    def printBoard(self) -> None:
        print("-" *9)
        for row in self.rows:
            print(row)
        print("-" *9)

    def setValue(self, row, column, value) -> None:
        self.rows[row][column] = value

    # Check if the board is goal state
    def isSolution(self) -> bool:
        return [value for (_, _, value) in self.getBoardData()] == list(range(1, 9)) + [0]

    # Return coordinates of empty point on board
    def findZero(self) -> List[int]:
        for row, column, value in self.getBoardData():
            if value == 0: return (row, column)
        raise RuntimeError("Could not find '0'. Something went wrong.")

    def __str__(self):
        s = ""
        for row in self.rows:
            s += "".join([str(x) for x in row])
        return s
