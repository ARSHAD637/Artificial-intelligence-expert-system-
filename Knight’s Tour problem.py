import sys
sys.setrecursionlimit(10000)  # Increase recursion depth if needed

N = 8  # Board size

# All knight moves
moves = [(-2, -1), (-1, -2), (1, -2), (2, -1),
         (2, 1), (1, 2), (-1, 2), (-2, 1)]

def is_valid(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def print_board(board):
    for row in board:
        print(' '.join(str(cell).zfill(2) for cell in row))

def knights_tour(x, y, movei, board):
    if movei == N * N:
        return True

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if is_valid(nx, ny, board):
            board[nx][ny] = movei
            if knights_tour(nx, ny, movei + 1, board):
                return True
            board[nx][ny] = -1  # Backtrack

    return False

def solve():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    start_x, start_y = 0, 0  # You can change these
    board[start_x][start_y] = 0

    if knights_tour(start_x, start_y, 1, board):
        print("Knight's tour found:")
        print_board(board)
    else:
        print("No solution exists for starting position ({},{})".format(start_x, start_y))

solve()
