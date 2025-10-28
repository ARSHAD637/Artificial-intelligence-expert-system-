def solve_eight_queens():
    n = 8
    board = [[0]*n for _ in range(n)]
    cols = set()
    diag1 = set()   # r - c
    diag2 = set()   # r + c

    def backtrack(r):
        if r == n:
            return True
        for c in range(n):
            if c in cols or (r-c) in diag1 or (r+c) in diag2:
                continue
            board[r][c] = 1
            cols.add(c); diag1.add(r-c); diag2.add(r+c)
            if backtrack(r+1):
                return True
            board[r][c] = 0
            cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)
        return False

    backtrack(0)
    return board

if __name__ == "__main__":
    solution = solve_eight_queens()
    for row in solution:
        print(" ".join(map(str, row)))




output
1 0 0 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 0 0 0 1
0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0
0 0 0 0 0 0 1 0
0 1 0 0 0 0 0 0
0 0 0 1 0 0 0 0

