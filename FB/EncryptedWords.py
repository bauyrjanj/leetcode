
def findEncryptedWord(s):
    if len(s )==0:
        return ""

    mid = (len(s ) -1 )//2

    return s[mid] +findEncryptedWord(s[:mid]) +findEncryptedWord(s[mid +1:])

if __name__ == "__main__":

    print(findEncryptedWord("abcxcba"))