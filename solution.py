"""
Data class that stores information about a board's solution.
Can also print out the statistics.
"""
class SolutionInfo:
    def __init__(self, searchName: str, h: str, boardString: str, bestSolution: int, maxQueue: int, duration: float, totalExplored: int):
        self.searchName = searchName
        self.heuristicName = h
        self.boardString = boardString
        self.bestSolution = bestSolution
        self.maxQueue = maxQueue
        self.duration = duration
        self.totalExplored = totalExplored

    def print_info(self):
        print(f"Search Algorithm: {self.searchName}")
        print(f"Heuristic: {self.heuristicName}")
        if self.bestSolution == None:
            print("No solution was found. The board was unsolvable.")
        else:
            print(f"Solution was found at depth: {self.bestSolution}")
        print(f"Max Queue Size: {self.maxQueue}")
        print(f"Total Explored States: {self.totalExplored}")
        print(f"Total Time Taken by Search: {self.duration:.3f} seconds")
       