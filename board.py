from typing import List, Tuple
from heapq import heappush, heappop
import time

from solution import SolutionInfo
from heuristics import manhattan, misplaced, null_heuristic

mapping = {
    null_heuristic : ("Uniform Cost Search", "Null Heuristic"),
    misplaced : ("A* Search", "Misplaced Tile"),
    manhattan : ("A* Search", "Manhattan Distance")
}

class Board:
    SOLUTION = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    def __init__(self, *args):
        if not args:
            raise RuntimeError("Cannot instantiate empty Board.")
        if isinstance(values := args[0], tuple):
            if len(values) != 9:
                raise RuntimeError("Board must 9 values.")
            #self.rows = copy.deepcopy(rows)
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
            raise RuntimeError("Cannot do this, fix this alter")

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
        return self.values[row*3 + column]

    def getBoardData(self) -> List[List[int]]:
        res = [0] * 9
        for i in range(9):
            row = i // 3
            column = i % 3
            res[i] = (row, column, self.values[row*3 + column])
        return res

    def printBoard(self) -> None:
        print("-" *9)
        for i in range(0, 9, 3):
            print(self.values[i:i+3])
        print("-" *9)

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

    def solve(self, h, verbose = False) -> SolutionInfo:
        #if not self.can_solve:
        #    raise RuntimeError("Tried to solve unsolvable board.")
        
        seen = set([self.values])
        dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
        exploreCount = 0
        solutionDepth = None
        maxSize = 1

        start_time = time.perf_counter()
        i = 0
        heap = [ (h(self.values), 0, i, self)]
        
        while heap:
            if len(heap) > maxSize: maxSize = len(heap)
            _, depth, _, b = heappop(heap)
            exploreCount += 1

            if verbose:
                b.printBoard()
                print("")

            # Check if we have found solution
            if b.isSolution():
                solutionDepth = depth
                break

            # Find zero
            zeroY, zeroX = b.findZero()
            zeroIndex = zeroY * 3 + zeroX 
            for deltaX, deltaY in dirs:
                newX, newY = zeroX + deltaX, zeroY + deltaY
                if 0 <= newX < 3 and 0 <= newY < 3:
                    # Then, it is possible to swap
                    index = newY * 3 + newX
                    newList = list(b.values)
                    newList[zeroIndex], newList[index] = newList[index], newList[zeroIndex]
                    newBoard = Board(tuple(newList))

                    # Don't add previously seen boards to queue
                    if newBoard.values not in seen:
                        i += 1
                        heappush(heap, (h(newBoard.values) + depth + 1, depth + 1, i, newBoard ))
                        seen.add(newBoard.values)
        
        end_time = time.perf_counter()
        elapsedTime = end_time-start_time # time taken in seconds
        searchName, heuristicName = mapping[h]
        return SolutionInfo(searchName, heuristicName, str(self), solutionDepth, maxSize, elapsedTime, exploreCount)
