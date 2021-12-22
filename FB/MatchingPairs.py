def matchingPairs(s, t):
    not_equal = []
    swap = False
    r = 0

    if s == t:
        r = len(s) - 2
    else:
        for i in range(len(s)):
            if s[i] != t[i]:
                not_equal.append(i)
            else:
                r += 1

        for idx in not_equal:
            try:
                replace = s.index(t[idx])
            except Exception as e:
                replace = -1

            if replace != -1 and s[idx] == t[replace]:
                if swap:
                    r += 1
                else:
                    r += 2
                break
            if replace != -1 and s[idx] != t[replace] and not swap:
                r += 1
                swap = True

    return r

if __name__ == "__main__":

    s1 = "abcd"
    t1 = "adcb"
    print(matchingPairs(s1,t1))

    s2 = "mno"
    t2 = "mno"
    print(matchingPairs(s2, t2))