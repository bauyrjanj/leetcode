# Recursive approach
def dfs(grid, s, e):
    directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]
    if s==e:
        return True
    print(s)
    x, y = s
    for direction in directions:
        nx, ny = x, y
        while 0<=nx+direction[0]<len(grid) and 0<=ny+direction[1]<len(grid[0]) and grid[nx+direction[0]][ny+direction[1]]==0:
            nx+=direction[0]
            ny+=direction[1]

        if (nx, ny) not in visited:
            visited.add((nx, ny))
            dfs(grid, (nx, ny), e)

    return False



if __name__=="__main__":
    m = [[0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0],
         [1, 1, 0, 1, 1],
         [0, 0, 0, 0, 0]]

    visited = set()
    Path = []
    print(dfs(m, (0, 4), (4, 4)))

