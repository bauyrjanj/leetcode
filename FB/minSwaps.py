def minSwaps(arr):
    n = len(arr)
    swap = 0
    visited = [False]*n

    for i in range(n):
        if arr[i]==i+1 or visited[i]:
            continue
        else:
            visited[i], visited[arr[i]-1] = True, True
            swap+=1

    return swap


if __name__ == "__main__":
    arr = [3,1,2] # Numbers are consecutive.
    print(minSwaps(arr))

