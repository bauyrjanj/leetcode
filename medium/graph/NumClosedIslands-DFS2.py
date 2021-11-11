from collections import deque

def dfs(grid):
    nrow = len(grid)
    ncol = len(grid[0])
    no_island = 0
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    d = deque()
    visited = set()

    for row in range(nrow):
        for col in range(ncol):
            if grid[row][col]==0 and (row, col) not in visited:
                d.append((row, col))
                visited.add((row, col))
                isClosed = True # First assume the island is closed

                while d:
                    r, c = d.popleft()
                    if r in [0, nrow-1] or c in [0, ncol-1]:
                        isClosed = False # if right on the edge/boundary then it cant be a closed island

                    for direction in directions: # Then look at the neighbors of the position
                        nr, nc = r+direction[0], c+direction[1]
                        if 0 <= nr < nrow and 0 <= nc < ncol and grid[nr][nc]==0 and (nr, nc) not in visited:
                            d.append((nr, nc))
                            visited.add((nr, nc))
                if isClosed:
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