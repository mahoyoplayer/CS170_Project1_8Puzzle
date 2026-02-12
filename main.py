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

# Map of solution depth to pre-generated board strings
testBoards = {
    0: "123456780",
    2: "123456078",
    4: "123506478",
    8: "136502478",
    12: "136507482",
    16: "167503482",
    20: "712485630",
    24: "072461358"
}

INDENT = "  "

def main():
    print("8-Puzzle Solver", end = "\n\n")
    createPrompt = f"Choose: \n{INDENT}(1) Create your own board\n{INDENT}(2) Use a pre-generated board\n\nEnter '1' or '2': "
    while (createChoice := input(createPrompt)) and createChoice not in ["1", "2"]:
        print('Invalid input. Please enter either "1" or "2".', end = "\n\n")
    print("")

    b = None
    if createChoice == "1":
        # User enters their own board
        prevUsed = []
        for i in range(3):
            while True:
                valid = True
                row = input(f"Enter Row #{i+1}: ").split()
                if len(row) != 3:
                    print("Entered row was not of expected length (3). Please try again.\n")
                    continue

                currUsed = []
                for j in range(3):
                    # Verify all inputs are positive integers
                    if not row[j].isdigit():
                        valid = False
                        break
                    row[j] = int(row[j])
                    # Verify we are not using previously used numbers
                    if 0 <= row[j] < 9 and row[j] not in currUsed and row[j] not in prevUsed:
                        currUsed.append(row[j])
                    else:
                        valid = False
                        break
                
                if not valid:
                    print("\nInvalid row entered. Make sure your input meets the following requirements.")
                    print(f'{INDENT}1. Is in the format "a b c" where a, b, and c are different integers between 0 and 8.')
                    print(f'{INDENT}2. Rows cannot contain integers used in previous rows.{f" You have already used {prevUsed}." if prevUsed else ""}\n')
                    continue

                prevUsed.extend(currUsed)
                break
        b = Board(tuple(prevUsed))
    else:
        # User selects pre-generated board
        while True:
            depth_choice = input("Choose depth of pre-generated board: (0, 2, 4, 8, 12, 16, 20, 24): ")
            bad_input = False
            if not depth_choice.isdigit():
                print("Invalid input. Did not receive a proper integer.", end = "\n\n")
                continue
            depth_choice = int(depth_choice)
            if depth_choice not in testBoards:
                print("Invalid input. Did not select a depth from the list above.", end = "\n\n")
                continue
            boardString = testBoards[int(depth_choice)] 
            b = Board(boardString)
            break

    h_map = {
        "A": null_heuristic,
        "B": misplaced,
        "C": manhattan
    }

    # Get user choice for algorithm
    print("\nAlgorithms")
    print(f"{INDENT}A: Uniform Cost Search")
    print(f"{INDENT}B: A* with Misplaced Tile Heuristic")
    print(f"{INDENT}C: A* with Manhattan Distance Heuristic")
    while (h_choice := input("\nChoose an algorithm: ")) not in h_map:
        print('Invalid input, try again. Please enter "A", "B", or "C".\n')
    
    # Print out trace of problem as well as final stats.
    print("")
    sol = b.solve(h_map[h_choice], verbose = True)
    print("Final Results: ")
    sol.print_info()
    print("")

if __name__ == "__main__":
    main()

