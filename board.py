from typing import List
import copy
from heapq import heappush, heappop
import time

from solution import SolutionInfo
from heuristics import manhattan, misplaced, null_heuristic



class Board:
    BOARD_SIZE = 3
    SOLUTION = "123456780"

    def __init__(self, *args):
        if not args:
            raise RuntimeError("Cannot instantiate empty Board.")
        if isinstance(rows := args[0], list):
            if len(rows) != self.BOARD_SIZE:
                raise RuntimeError("Board must three rows.")
            elif False in [len(row) == self.BOARD_SIZE for row in rows]:
                raise RuntimeError("Board can only have three values in each row.")
            self.rows = copy.deepcopy(rows)
            
        elif isinstance(s := args[0], str):
            if len(s) != 9:
                raise RuntimeError(f"Board can only have 9 elements. Received {len(s)}")
            if sorted(s) != sorted(Board.SOLUTION):
                raise RuntimeError(f"Tried to instantiate board with invalid elements - {s}")
            self.rows = []
            for i in range(3):
                self.rows.append([])
                for j in range(3):
                    self.rows[-1].append(int(s[i*3 + j]))
        self.can_solve = Board.solvable(str(self))

    @staticmethod
    def solvable(s: str):
        def inversionCount(board: str) -> int:
            nums = [int(c) for c in board if c != "0"]
            total = 0
            for i in range(len(nums)):
                for j in range(i+1, len(nums)):
                    if nums[i] > nums[j]:
                        total += 1
            return total
        """
        def inversionCount(board: str) -> bool:
            total = 0
            found = [0] * 9
            for num in [int(c) for c in board]:
                if num == 0: continue
                total += sum(found[num:])
                found[num-1] = 1
            return total
        # Inversion count must be even to be valid
        """
        return inversionCount(s) % 2 == 0

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
        return "".join(str(value) for (_, _, value) in self.getBoardData()) == Board.SOLUTION

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

    def solve(self, h, verbose = False) -> SolutionInfo:
        if not self.can_solve:
            raise RuntimeError("Tried to solve unsolvable board.")
        
        seen = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        exploreCount = 0
        bestSol = None
        maxSize = 1

        start_time = time.perf_counter()
        i = 0
        heap = [ (h(self), 0, i, self)]
        

        while heap:
            if len(heap) > maxSize: maxSize = len(heap)
            _, depth, _, b = heappop(heap)
            exploreCount += 1

            # Check if we have found solution
            if b.isSolution():
                bestSol = depth
                break

            seen.add(str(b))

            # Find zero
            zeroX, zeroY = b.findZero()
            for deltaX, deltaY in dirs:
                newX, newY = zeroX + deltaX, zeroY + deltaY
                if 0 <= newX < 3 and 0 <= newY < 3:
                    # Then, we can swap
                    newBoard = Board(b.rows)

                    temp = newBoard.getValue(newX, newY)
                    newBoard.setValue(newX, newY, 0)
                    newBoard.setValue(zeroX, zeroY, temp)
                    if verbose:
                        newBoard.printBoard()
                        print("")

                    if str(newBoard) not in seen:
                        i += 1
                        heappush(heap, (h(newBoard) + depth + 1, depth + 1, i, newBoard ))
        end_time = time.perf_counter()

        mapping = {
            null_heuristic : ("Uniform Cost Search", "Null Heuristic"),
            misplaced : ("A* Search", "Misplaced Tile"),
            manhattan : ("A* Search", "Manhattan Distance")
        }
        searchName, heuristicName = mapping[h]
        elapsedTime = end_time-start_time # in seconds
        
        return SolutionInfo(searchName, heuristicName, str(self), bestSol, maxSize, elapsedTime, exploreCount)
