from collections import deque

def shortest_path(grid):
    nrows, ncols = len(grid), len(grid[0])

    d = deque()
    d.append((0, 0, 0))  # start, end, step

    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    visited = set()

    while d:
        cr, cc, cdist = d.popleft()

        if cr == nrows - 1 and cc == ncols - 1 and grid[cr][cc]!=1:
            return cdist

        if grid[cr][cc] == 1:
            continue

        for direction in directions:
            nr = cr + direction[0]
            nc = cc + direction[1]

            if 0 <= nr < nrows and 0 <= nc < ncols and (nr, nc) not in visited:
                d.append((nr, nc, cdist + 1))
                visited.add((nr, nc))

    return -1

if __name__ == "__main__":
    grid = [[0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 1, 1, 1],
            [0, 0, 0, 0, 0]]

    print(shortest_path(grid))

