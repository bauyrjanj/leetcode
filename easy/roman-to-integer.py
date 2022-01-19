
def roman_to_integer(s):
    hmap = {"I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000}
    num = 0
    for i in range(len(s)-1):
        if hmap[s[i+1]]//hmap[s[i]] in [5, 10]:
            num+=-1*hmap[s[i]]
        else:
            num+=hmap[s[i]]
    num += hmap[s[-1]]

    return num


if __name__ == "__main__":
    print(roman_to_integer("MCMXCIV"))

