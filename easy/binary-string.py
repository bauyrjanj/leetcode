
def binary_string(s):
    s = list(map(len, s.replace("01", "1 0").replace("10", "1 0").split()))
    return sum(min(a, b) for a, b in zip(s, s[1:]))

if __name__ == "__main__":
    s = "00110011"
    print(binary_string(s))