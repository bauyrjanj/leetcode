def perm(arr):
    res = []
    def backtrack(arr, path = []):
        if not arr:
            res.append(path)
        for i in range(len(arr)):
            backtrack(arr[:i]+arr[i+1:], path+[arr[i]])

    backtrack(arr)

    return res

if __name__ == "__main__":
    arr = [3,1,2]
    print(perm(arr))

