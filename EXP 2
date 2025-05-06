N = 8

def print_solution(board):
    for row in board:
        line = ""
        for cell in row:
            line += "Q " if cell else ". "
        print(line)
    print()

def is_safe(board, row, col):
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False
    return True

def solve_n_queens(board, row):
    if row >= N:
        print_solution(board)
        return True
    res = False
    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1
            res = solve_n_queens(board, row + 1) or res
            board[row][col] = 0
    return res

def solve():
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0)

solve()

