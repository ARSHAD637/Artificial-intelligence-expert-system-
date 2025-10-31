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


output:
00 59 38 33 30 17 08 63
39 34 31 60 09 62 29 16
58 01 40 49 32 27 18 07
35 48 41 28 61 10 15 26
42 57 02 53 50 45 06 19
47 36 55 44 25 20 11 14
56 43 52 03 54 23 24 05
37 46 51 40 21 12 13 22
​

