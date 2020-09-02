
# with open('czy_input3.txt', 'r') as f:
#     M, N = map(int, f.readline().strip().split(','))
#
#     kingdom = [list(f.readline().strip()) for _ in range(M)]

import sys
M, N = map(int, sys.stdin.readline().strip().split(','))
kingdom = [list(sys.stdin.readline().strip()) for _ in range(M)]


def dfs(grid, r, c):
    grid[r][c] = 0
    nr, nc = len(grid), len(grid[0])
    for x, y in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= x < nr and 0 <= y < nc and grid[x][y] == "S":
            dfs(grid, x, y)


def numIslands(grid):
    nr = len(grid)
    if nr == 0:
        return 0
    nc = len(grid[0])
    num_islands = 0
    for r in range(nr):
        for c in range(nc):
            if grid[r][c] == "S":
                num_islands += 1
                dfs(grid, r, c)

    return num_islands

print(numIslands(kingdom))
