def gridtraveler(r, c, memo = {}):
    if (r,c) in memo:
        return memo[(r,c)]
    if r<=0 or c<=0:
        return 0

    if r==1 and c==1:
        return 1
    memo[(r,c)] = gridtraveler(r-1, c, memo)+gridtraveler(r, c-1, memo)

    return memo[(r,c)]

if __name__ == "__main__":
    print(gridtraveler(4,4))

    