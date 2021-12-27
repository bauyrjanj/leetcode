def findMinArray(arr, k):
    if k == 0:
        return arr

    if arr[k] < arr[0]:
        arr[k - 1], arr[k] = arr[k], arr[k - 1]
        k -= 1
        return findMinArray(arr, k)
    else:
        smallest = arr.index(min(arr[k + 1:]))
        arr[smallest - 1], arr[smallest] = arr[smallest], arr[smallest - 1]
        smallest -= 1
        k -= 1
        return findMinArray(arr, k)


if __name__ == "__main__":
    arr = [2, 1, 7, 4, 2]
    k = 3
    print(findMinArray(arr, k))

    