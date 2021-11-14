from collections import defaultdict, deque

def printMatrixDiagonal(mat, n):
    # Initialize indexes of element to be printed next
    r = 0
    c = 0
    k = 0

    # Direction is initially from down to up
    isUp = True

    # Traverse the matrix till all elements get traversed
    while k < n * n:
        # If isUp = True then traverse from downward
        # to upward
        if isUp:

            # right
            while r >= 0 and c < n:
                print(str(mat[r][c]), end=" ")
                k += 1
                c += 1
                r -= 1

            # Set i and j according to direction
            if r < 0 and c <= n - 1:
                r = 0

            if c == n:
                r = r + 2
                c -= 1

        # If isUp = 0 then traverse up to down
        else:
            while c >= 0 and r < n:
                print(mat[r][c], end=" ")
                k += 1
                r += 1
                c -= 1

            # Set i and j according to direction
            if c < 0 and r <= n - 1:
                c = 0
            if r == n:
                c = c + 2
                r -= 1

        # Revert the isUp to change the direction
        isUp = not isUp


def traverseDiagonal1(n, M):
    table = defaultdict(list)
    result = []
    for r in range(n):
        for c in range(n):
            table[r + c].append(M[r][c])

    for k, v in table.items():
        if k % 2 == 0:
            v.reverse()
            result += v
        else:
            result += v

    return result


def traverseDiagonal2(n, mat):
    r = c = 0
    k = n * n
    result = []

    for i in range(k):
        result.append(mat[r][c])
        if (r + c) % 2 == 0:  # go up
            if c == n - 1:
                r += 1
            elif r == 0:
                c += 1
            else:
                r -= 1
                c += 1
        else:  # go down
            if r == n - 1:
                c += 1
            elif c == 0:
                r += 1
            else:
                r += 1
                c -= 1
    return result



def traverse_diag(mat):
    nrow, ncol = len(mat), len(mat[0])
    # directions = [[1, -1], [-1, 1], [0, 1], [0, -1], [1, 0]]
    directions = [[0, 1], [1, -1], [1, 0], [-1, 1]] # right, down diag., straight down, up diag.
    visited = set()
    d = deque()
    result = []

    r = c = 0
    d.append((r,c))
    visited.add((r,c))
    result.append(mat[r][c])  # main operation

    while d:
        cr, cc = d.popleft()
        if cr == nrow-1 and cc==ncol-1: # condition to end the traversal
            return result

        for direction in directions:    # directions
            nr, nc = cr+direction[0], cc+direction[1]
            if 0<=nr<=nrow-1 and 0<=nc<=ncol-1 and (nr, nc) not in visited:
                d.append((nr, nc))
                visited.add((nr, nc))
                result.append(mat[nr][nc])

    return -1


if __name__ == "__main__":
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    print(traverse_diag(mat))
