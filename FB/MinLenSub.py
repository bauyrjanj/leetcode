from collections import Counter

def MinLenSubstring(s,t):
    cmap = Counter()

    for c in t:
        cmap[c]+=1

    count = len(cmap.keys())
    N = len(s)
    i = j = left = 0
    right = N-1
    minLen = N
    found = False

    while j<N:
        char = s[j]
        j+=1
        if char in cmap:
            cmap[char]-=1
            if cmap[char]==0:
                count-=1

        if count>0:
            continue

        while count==0 and i<N:
            c = s[i]
            i+=1
            if c in cmap:
                cmap[c]+=1
                if cmap[c]>0:
                    count+=1

        if j-i<minLen:
            left = i
            right = j
            minLen = j-i
            found = True

        result = -1
        if found:
            result = len(s[left-1:right])

        return result

if __name__ == "__main__":
    s = "dcbefebce"
    t = "fd"
    print(MinLenSubstring(s,t))