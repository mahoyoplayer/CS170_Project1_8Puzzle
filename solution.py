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
        print(f"Search: {self.searchName}")
        print(f"Heuristic: {self.heuristicName}")
        print(f"Board: {self.boardString}")
        print(f"Best Solution Cost: {self.bestSolution}")
        print(f"Max Queue Size: {self.maxQueue}")
        print(f"Duration: {self.duration:.4f} seconds")
        print(f"Total Explored Nodes: {self.totalExplored}")

"""
I want - 
    what heuristic was used
    the string of the original board

    depth of the best solution
    maximum nodes in queue
    time it took to find solution
"""