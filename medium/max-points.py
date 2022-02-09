
# first and last row matters -> max(values_sum), min(idx_diff)
# select the max of middle rows

def max_points(arr):
    max_first = max_last = ans = 0

    first = arr[0]
    last = arr[-1]

    for i in range(1,len(arr)-1):
        ans+=max(arr[i])

    for i in range(len(first)):
        max_first = max(max_first, abs(first[i]-i))
        max_last = max(max_last, abs(last[i] - i))


    return ans+max_first+max_last


if __name__ == "__main__":
    arr = [[1,2,3],
           [1,5,1],
           [3,1,1]]

    arr2 = [[5,2,1,2],
            [2,1,5,2],
            [5,5,5,0]]


    print(max_points(arr2))