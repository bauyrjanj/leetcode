def f(s1, s2):
    if len(s1)>=len(s2):
        return False
    d = {}
    for c in s1:
        if c in d:
            d[c]+=1
        else:
            d[c]=1

    for c in s2:
        if c in d:
            d[c]-=1
        else:
            d[c]=-1

    counter = 0
    for k, v in d.items():
        if v==-1:
            counter+=1
        elif v<-1:
            return False
        else:
            pass
    return counter==1


if __name__ == "__main__":
    print(f("EST", "TEST"))
    print(f("ACT", "CART"))
    print(f("ACT", "AACTR"))
    print(f("ACT", "AATR"))
    print(f("ACT", "AACT"))

    