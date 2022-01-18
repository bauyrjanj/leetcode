
def longest_prefix(arr):
    shortest = min(arr, key=len)
    for i, c in enumerate(shortest):
        for other in arr:
            if other[i]!=c:
                return shortest[:i]

    return shortest

if __name__ == "__main__":
    strs = ["flower", "flow", "flight"]
    # strs = ["dog", "racecar", "car"]
    print(longest_prefix(strs))
