def is_safe(board, row, col):
    """
    Check if placing a queen at board[row][col] is safe.
    """
    for prev_row in range(row):
        placed = board[prev_row]
        # Same column check
        if placed == col:
            return False
        # Diagonal check
        if abs(prev_row - row) == abs(placed - col):
            return False
    return True


def solve_n_queens(n):
    """
    Solves the N-Queens problem using backtracking.
    Returns all solutions and the count of backtracks.
    """
    board = [-1] * n
    solutions = []
    backtrack_count = [0]

    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return

        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # Undo placement
                
        backtrack_count[0] += 1  # Track backtracks

    backtrack(0)
    return solutions, backtrack_count[0]


def display_board(solution, n):
    """
    Pretty-prints an N-Queens solution grid.
    """
    border = " +" + "---+" * n
    print(border)
    for row in range(n):
        print(" |", end="")
        for col in range(n):
            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")
        print()
        print(border)


if __name__ == "__main__":
    # --- Solve for N=4, N=6, and N=8 ---
    for n in [4, 6, 8]:
        solutions, backtracks = solve_n_queens(n)
        print(f"N={n}: {len(solutions)} solutions, {backtracks} backtracks")

        if n == 4:
            print(f"\nAll solutions for {n}-Queens:")
            for i, sol in enumerate(solutions, 1):
                print(f"\nSolution {i}: {sol}")
                display_board(sol, n)
            print("-" * 30)
