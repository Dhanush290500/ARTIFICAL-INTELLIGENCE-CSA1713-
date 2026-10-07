def get_user_puzzle():
    """Prompts the user to enter a custom puzzle state and validates it."""
    print("Enter your custom 8-puzzle start state.")
    print("Use numbers 0-8 separated by spaces, where 0 is the blank space.")
    print("Example: 1 2 3 4 0 5 6 7 8\n")
    
    while True:
        try:
            user_input = input("Enter puzzle: ")
            # Split the input string by spaces and convert each piece to an integer
            state = tuple(int(x) for x in user_input.split())
            
            # Validation 1: Check if there are exactly 9 numbers
            if len(state) != 9:
                print("Error: You must enter exactly 9 numbers. Try again.\n")
                continue
                
            # Validation 2: Check if the numbers are exactly 0 through 8
            if set(state) != set(range(9)):
                print("Error: You must use each number from 0 to 8 exactly once. Try again.\n")
                continue
                
            return state
            
        except ValueError:
            print("Error: Please enter only valid integers separated by spaces. Try again.\n")


# --- Example Usage ---
if __name__ == "__main__":
    goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)
    
    # Call the new function to get user input
    initial = get_user_puzzle()
    
    print("\nInitial State:")
    print_board(initial)
    print("Solving... (this may take a moment for complex boards)")
    
    solution_path = solve_8_puzzle(initial, goal)
    
    if solution_path:
        print(f"\nSolved in {len(solution_path)} moves!\n")
        for step, (move, state) in enumerate(solution_path, 1):
            print(f"Step {step}: Move {move}")
            print_board(state)
    else:
        print("\nNo solution exists for this configuration.")
