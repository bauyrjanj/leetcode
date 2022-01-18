# Given a string s, return true if the s can be palindrome after deleting at most one character from it.
def valid_palindrome(s):
    start = 0
    end = len(s)-1

    def validPalindromeUtil(s, i, j): # Regular palindrome
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    while start<end:
        if s[start]==s[end]:
            start+=1
            end-=1
        else:
            return validPalindromeUtil(s, start+1, end) or validPalindromeUtil(s, start, end-1)

    return True


if __name__ == "__main__":
    # s = "abc"
    # s = "abca"
    s = "deeee"
    print(valid_palindrome(s))
