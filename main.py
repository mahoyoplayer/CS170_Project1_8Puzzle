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

    while (createChoice := input("\nCreate own board or do pre-generated. 1 or 2: ")) and createChoice not in ["1", "2"]:
        print('\nInvalid input. Please enter either "1" or "2".')

    b = None
    if createChoice == "1":
        prevUsed = []
        # Enter your own board
        for i in range(3):
            while True:
                row = input(f"Enter Row {i+1}: ").split()
                try:
                    assert len(row) == 3
                    currUsed = []
                    for j in range(3):
                        # Verify input is a positive integer
                        assert row[j].isdigit()
                        row[j] = int(row[j])     
                        assert 0 <= row[j] < 9
                        if row[j] not in currUsed and row[j] not in prevUsed:
                            currUsed.append(row[j])
                        else:
                            assert False
                    prevUsed.extend(currUsed)
                    break
                except:
                    print("\nInvalid row entered. Make sure your input meets the following requirements.")
                    print(f'{INDENT}1. Is in the format "a b c" where a, b, and c are different integers between 0 and 8.')
                    print(f'{INDENT}2. Rows cannot contain integers used in previous rows.{f" You have already used {prevUsed}." if prevUsed else ""}\n')
        b = Board(tuple(prevUsed))
    else:
        depth_choice = None
        while True:
            depth_choice = input("\nEnter a depth: (0, 2, 4, 8, 12, 16, 20, 24): ")
            bad_input = False
            try:
                depth_choice = int(depth_choice)
                if depth_choice not in testBoards: assert False
                break
            except:
                print("Invalid input, try again. Please an integer within the values above.")

        boardString = testBoards[int(depth_choice)] 
        b = Board(boardString)

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
    
    
    sol = b.solve(h_map[h_choice], verbose = True)
    print("Final Results: ")
    sol.print_info()

if __name__ == "__main__":
    main()

