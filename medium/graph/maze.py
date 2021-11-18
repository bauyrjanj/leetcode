
# BFS - notice the usage of queue - iterative implementation
def maze_bfs(grid, s, e): # maze, start, end
    # Assume 1s are walls and 0s are open spaces
    from collections import deque
    r_start, c_start = s
    r_end, c_end = e
    nrow = len(grid)
    ncol = len(grid[0])

    if grid[r_start][c_start]==1 and grid[r_end][c_end]==1:
        return -1

    Path = []
    directions = [[-1,0], [1,0], [0,-1], [0,1]]
    d = deque()
    visited = set()
    d.append((r_start, c_start))
    visited.add((r_start, c_start))
    Path.append((r_start, c_start))

    while d:
        cr, cc = d.popleft()
        if grid[cr][cc] == 1:
            continue

        if cr==r_end and cc==c_end:
            return Path

        for direction in directions:
            nr, nc = cr+direction[0], cc+direction[1]
            if 0<=nr<=nrow-1 and 0<=nc<=ncol-1 and grid[nr][nc]==0 and (nr, nc) not in visited:
                d.append((nr, nc))
                visited.add((nr, nc))
                Path.append((nr, nc))

    return -1

# DFS - notice the usage of stack - iterative implementation

def maze_dfs(grid, s, e): # maze, start, end
    stack = []
    r_start, c_start = s
    stack.append((r_start, c_start))
    r_end, c_end = e
    nrow = len(grid)
    ncol = len(grid[0])
    visited = set()

    Path = []
    directions = [[0,1], [0,-1], [1,0], [-1,0]]


    while stack:
        cr, cc = stack.pop()
        if cr == r_end and cc == c_end:
            return Path

        for direction in directions:
            nr, nc = cr, cc
            while 0<=nr+direction[0]<=nrow-1 and 0<=nc+direction[1]<=ncol-1 and grid[nr+direction[0]][nc+direction[1]]==0:
                nr+=direction[0]
                nc+=direction[1]

            if (nr, nc) not in visited:
                visited.add((nr, nc))
                stack.append((nr, nc))
                Path.append((nr, nc))


    return -1

# DFS
from collections import namedtuple
WHITE, BLACK = range(2)
coordinate = namedtuple('Coordinate', ('x', 'y'))
def maze2(grid, s, e):
    def helper(cur):
        if not (0<=cur.x<len(grid) and 0<=cur.y<len(grid[0]) and grid[cur.x][cur.y]==WHITE):
            return False
        path.append(cur)
        grid[cur.x][cur.y]=BLACK

        if cur==e:
            return True
        if any(map(helper, map(coordinate, (cur.x-1, cur.x+1, cur.x, cur.x), (cur.y, cur.y, cur.y-1, cur.y+1)))):
            return True
        del path[-1]
        return False
    path = []
    helper(s)
    return path

if __name__=="__main__":
    grid = [[1, 1, 0, 0],
            [1, 1, 0, 1],
            [1, 1, 0, 1],
            [1, 0, 0, 1]]

    m = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]

    # [0, 4]
    # [4, 4]
    print(maze_dfs(m, (0,4), (4,4)))
    print(maze2(m, coordinate(0, 4), coordinate(4, 4)))


