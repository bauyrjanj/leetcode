def num_paths(r, c):
    if r==0 and c==0:
        return 1

    ways_top = 0 if r==0 else num_paths(r-1, c)
    ways_left = 0 if c==0 else num_paths(r, c-1)

    return ways_left+ways_top

if __name__ == "__main__":
    print(num_paths(3,3))