from typing import List
from math import factorial
from board import Board
from heuristics import manhattan, misplaced, null_heuristic

def get_permutations(s: str) -> List[str]:
    n = len(s)
    res = []
    curr = []
    used = [False] * n
    def backtrack():
        if len(curr) == n:
            res.append("".join(curr))
            return
        for i in range(n):
            if not used[i]:
                curr.append(s[i])
                used[i] = True
                backtrack()
                curr.pop()
                used[i] = False
    backtrack()
    assert len(res) == factorial(n)
    return res

if __name__ == "__main__":
    s = "123456780"
    b = Board(s)
    #sol = b.solve(null_heuristic)
    #sol.print_info()
    #exit()
    boards = get_permutations(s)
    print(f"Total Boards Generated = {len(boards)}")

    validBoards = []
    for boardString in boards:
        if Board.solvable(boardString):
            validBoards.append(boardString)
    print(f"Total Valid Boards Found = {len(validBoards)}")

    greatestDepth = 0
    for i, boardString in enumerate(validBoards):
        b = Board(boardString)
        sol_info = b.solve(manhattan)
        greatestDepth = max(greatestDepth, sol_info.bestSolution)
        if i % 1000 == 0:
            print(f"Currently on {i}")

    print(greatestDepth)



            
