from collections import deque

def dfs(grid):
    nrow = len(grid)
    ncol = len(grid[0])
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    d = deque()
    visited = set()
    no_island = 0

    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col]==1 and (row, col) not in visited:
                d.append((row, col))
                visited.add((row, col))
                while d:
                    r, c = d.popleft()
                    if grid[r][c]==1:
                        for direction in directions:
                            nr, nc = r+direction[0], c+direction[1]
                            if 0 <= nr < nrow and 0 <= nc < ncol and (nr, nc) not in visited:
                                d.append((nr, nc))
                                visited.add((nr, nc))

                no_island+=1

    return no_island


if __name__ == "__main__":
    # grid = [[1,1,1,1,1,1,1,0],
    #         [1,0,0,0,0,1,1,0],
    #         [1,0,1,0,1,1,1,0],
    #         [1,0,0,0,0,1,0,1],
    #         [1,1,1,1,1,1,1,0]]
    #
    # grid = [[1, 1, 1],
    #         [1, 0, 1],
    #         [1, 1, 1]]

    # grid = [
    #     [1, 1, 1, 1, 0],
    #     [1, 1, 0, 1, 0],
    #     [1, 1, 0, 0, 0],
    #     [0, 0, 0, 0, 0]
    # ]
    grid = [[1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
            [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
            [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]]
    print(dfs(grid))