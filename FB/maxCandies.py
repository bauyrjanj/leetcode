import math

def maxCandies(arr, k):
    arr.sort()
    refill = []
    ate = 0

    while k>0:
        candy = arr.pop()
        if (refill and candy>=refill[0]) or not refill:
            ate+=candy
            refill.append(math.floor(candy/2))
            refill.sort(reverse=True)
        elif refill and candy<refill[0]:
            ate+=refill.pop(0)

        k-=1
    return ate

if __name__ == "__main__":
    arr = [2, 1, 7, 4, 2]
    k = 3
    print(maxCandies(arr, k))

