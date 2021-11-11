visited = set()
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def isValid(x, y, nrow, ncol, grid):
    if x<0 or x>=nrow or y<0 or y>=ncol or (x, y) in visited:
        return False
    return True


def dfs(cr, cc, grid):
    nrow, ncol = len(grid), len(grid[0])
    if nrow==0 or ncol==0:
        return -1

    visited.add((cr, cc))
    print(grid[cr][cc])

    for direction in directions:
        nr, nc = cr+direction[0], cc+direction[1]
        if isValid(nr, nc, nrow, ncol, grid):
            dfs(nr, nc, grid)


if __name__ == "__main__":
    grid = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    # grid = [[]]

    dfs(0,0,grid)

