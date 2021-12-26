def balance_brackets(s):
    h = {"{":"}",
          "(":")",
          "[":"]"}
    left = []

    for c in s:
        if c in h:
            left.append(c)
        elif c in h.values() and (left and h[left.pop()]!=c):
            return False
        else:
            pass

    return not left


if __name__ == "__main__":
    s = "{({[]})}"
    print(balance_brackets(s))









