from typing import List, Tuple, Callable
from heapq import heappush, heappop
import time

from solution import SolutionInfo
from heuristics import manhattan, misplaced, null_heuristic

# Map heuristic functions to names
mapping = {
    null_heuristic : ("Uniform Cost Search", "Null Heuristic"),
    misplaced : ("A* Search", "Misplaced Tile"),
    manhattan : ("A* Search", "Manhattan Distance")
}

INDENT = "  "

class Board:
    SOLUTION = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    # Constructor
    def __init__(self, *args):
        if not args or len(args) != 1:
            raise RuntimeError("Board instantiated with wrong parameters")
        if isinstance(values := args[0], tuple):
            if len(values) != 9:
                raise RuntimeError("Board must 9 values.")
            # Add validation here later
            self.values = values
        elif isinstance(s := args[0], str):
            if len(s) != 9 and len(set(c for c in s)) != 9:
                raise RuntimeError(f"Board can only have 9 unique elements. Received {len(s)}")
            for char in s:
                if int(char) not in self.SOLUTION:
                    raise RuntimeError(f"Tried to instantiate board with invalid elements - {char}")    
                
            self.values = tuple(int(c) for c in s)
        else:
            raise RuntimeError("Board instantiated with wrong type.")

    def getValue(self, row: int, column: int) -> int:
        return self.values[row*3 + column]

    # Return values of board alongside row and column coordinates
    def getBoardData(self) -> List[List[int]]:
        res = [0] * 9
        for i in range(9):
            row = i // 3
            column = i % 3
            res[i] = (row, column, self.values[row*3 + column])
        return res

    # Print board in pretty grid format
    def printBoard(self) -> None:
        print(" " + "-" *11)
        for i in range(0, 9, 3):
            print("| ", end = "")
            print(" | ".join(str(val) for val in self.values[i:i+3]), end = "")
            print(" |")
            print(" " + "-" *11)

    # Check if the board is goal state
    def isSolution(self) -> bool:
        return self.values == Board.SOLUTION

    # Return coordinates (row, column) of empty point on board
    def findZero(self) -> List[int]:
        for i, num in enumerate(self.values):
            if num == 0:
                return (i // 3, i % 3)
        raise RuntimeError("Could not find '0'. Something went wrong.")

    def __str__(self):
        return "".join(str(num) for num in self.values)

    # Returns information about board's solution with the option of output
    def solve(self, h: Callable, verbose: bool = False) -> SolutionInfo:
        seen = set()
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        exploreCount = 0
        solutionDepth = None
        maxSize = 1

        start_time = time.perf_counter()
        i = 0
        heap = [ (h(self.values), 0, i, self)]
        
        while heap:
            if len(heap) > maxSize: maxSize = len(heap)
            f, g, _, b = heappop(heap)
            if b.values in seen: continue
            exploreCount += 1

            if verbose:
                print(f"Current Board #{exploreCount}")
                h_value = f - g
                print(f"The current best board to expand has f(n) = {f} from h(n) = {h_value} and g(n) = {g}.", end = "\n\n")
                b.printBoard()
                print("\n")

            # Check if is goal state.
            if b.isSolution():
                if verbose:
                    print("Found Goal Board!", end = "\n\n\n")
                solutionDepth = g
                break

            seen.add(b.values)
            # Find the location of the empty tile
            zeroY, zeroX = b.findZero()
            zeroIndex = zeroY * 3 + zeroX 
            # Find all possible moves
            for deltaX, deltaY in dirs:
                newX, newY = zeroX + deltaX, zeroY + deltaY
                if 0 <= newX < 3 and 0 <= newY < 3:
                    # Move number into empty tile.
                    index = newY * 3 + newX
                    newList = list(b.values)
                    newList[zeroIndex], newList[index] = newList[index], newList[zeroIndex]
                    newBoard = Board(tuple(newList))

                    i += 1
                    heappush(heap, (h(newBoard.values) + g + 1, g + 1, i, newBoard ))
        
        end_time = time.perf_counter()
        elapsedTime = end_time-start_time # time taken in seconds
        searchName, heuristicName = mapping[h]
        return SolutionInfo(searchName, heuristicName, str(self), solutionDepth, maxSize, elapsedTime, exploreCount)