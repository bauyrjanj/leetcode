def firstUniqChar(s):
    counter = {}
    for c in s:
        if c in counter:
            counter[c] += 1
        else:
            counter[c] = 1

    for k, v in counter.items():
        if v == 1:
            return s.index(k)

    return -1

if __name__ == "__main__":
    print(firstUniqChar("leetcode"))