from board import Board
from heuristics import manhattan, null_heuristic, misplaced

"""
Report Link
https://docs.google.com/document/d/1EuaSfyVOmH6oO5BKkVf7cM13KElzivaVgpwU0cvI5j4/edit?tab=t.2xgeqygu6rx2


You can hardcode an initial state for testing purposes. 
But I want to be able to enter an arbitrary initial state. 
So sometime along the lines of the interface on the next page would be nice.

https://www.dropbox.com/scl/fi/c842lv0m28rjj8si36nda/Project_1_The_Eight_Puzzle_CS_170_2026.pdf?rlkey=032lxqgkk33zq7gov604tr5ko&e=2&dl=0
"""


testBoards = {
    0: "123456780",
    2: "123456078",
    4: "123506478",
    8: "136507482",
    12: "136507482",
    16: "167503482",
    20: "712485630",
    24: "072461358"
}

INDENT = "  "

def main():
    print("8-Puzzle Solver")
    print("Test Boards")

    depth_choice = None
    while True:
        depth_choice = input("\nEnter a depth: (0, 2, 4, 8, 12, 16, 20, 24): ")
        bad_input = False
        try:
            depth_choice = int(depth_choice)
            if depth_choice not in testBoards: bad_input = True
        except:
            bad_input = True
        if bad_input:
            print("Invalid input, try again. Please an integer within the values above.\n")
        else:
            break
        

    h_map = {
        "A": null_heuristic,
        "B": misplaced,
        "C": manhattan
    }
    print("\nAlgorithms")
    print(f"{INDENT}A: Uniform Cost Search")
    print(f"{INDENT}B: A* with Misplaced Tile Heuristic")
    print(f"{INDENT}C: A* with Manhattan Distance Heuristic")
    while (h_choice := input("\nChoose an algorithm: ")) not in h_map:
        print('Invalid input, try again. Please enter "A", "B", or "C".\n')
    
    boardString = testBoards[int(depth_choice)]
    b = Board(boardString)
    sol = b.solve(h_map[h_choice], verbose = True)
    print("Final Results: ")
    sol.print_info()

if __name__ == "__main__":
    main()

