'''
You are playing the Bulls and Cows game with your friend.

You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

The number of "bulls", which are digits in the guess that are in the correct position.
The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position.
Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.

Input: secret = "1", guess = "0"
Output: "0A0B"


Input: secret = "1", guess = "1"
Output: "1A0B"

'''

def bulls_and_cows(secret, guess):
    bull = cow = 0
    for i in range(len(guess)):
        if guess[i]==secret[i]:
            bull+=1
            secret = secret.replace(secret[i], 'B', 1)
            guess = guess.replace(guess[i], 'X', 1)

    for i in range(len(guess)):
        if guess[i] in secret:
            cow+=1
            secret = secret.replace(guess[i], 'C', 1)
    return f"{bull}A{cow}B"


if __name__=="__main__":
    # secret = "1123"
    # guess = "0111"

    # secret = "1807"
    # guess = "7810"

    secret = "11"
    guess = "10"
    print(bulls_and_cows(secret, guess))










