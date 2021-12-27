def getTotalTime(arr):
    penalty = 0
    arr.sort(reverse=True)

    while len(arr) > 1:
        a = arr.pop(0)
        b = arr.pop(0)
        penalty += a + b
        arr.insert(0, a + b)
    return penalty


if __name__ == "__main__":
    arr = [2, 1, 7, 4, 2]
    print(getTotalTime(arr))