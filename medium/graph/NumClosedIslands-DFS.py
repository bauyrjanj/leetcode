from collections import deque

def dfs(grid):
    nrow = len(grid)
    ncol = len(grid[0])
    no_island = 0
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    d = deque()

    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col]==0:
                d.append((row, col))
                grid[row][col]=1
                isClosed = True

                while d:
                    r, c = d.popleft()
                    if r in [0, nrow-1] or c in [0, ncol-1]:
                        isClosed = False

                    for direction in directions:
                        nr, nc = r+direction[0], c+direction[1]
                        if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc]==0:
                            d.append((nr, nc))
                            grid[nr][nc]=1
                if isClosed:
                    no_island+=1

    return no_island


if __name__ == "__main__":
    # grid = [[1,1,1,1,1,1,1,0],
    #         [1,0,0,0,0,1,1,0],
    #         [1,0,1,0,1,1,1,0],
    #         [1,0,0,0,0,1,0,1],
    #         [1,1,1,1,1,1,1,0]]
    grid = [
        [1, 1, 1, 1, 0],
        [1, 1, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # grid = [[1, 1, 1],
    #         [1, 0, 1],
    #         [1, 1, 1]]

    # grid = [[1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
    #         [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
    #         [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
    #         [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    #         [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    #         [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
    #         [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    #         [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
    #         [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
    #         [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    print(dfs(grid))









