# Brute force O(n) time
def findPeak(arr):
    for i in range(len(arr)-1):
        if i>0:
            if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
                return i

    return -1

# Optimized O(log n) time
def findPeak_Optimized(arr):
    start = 0
    end = len(arr)-1

    while start<end:
        mid = (end+start)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]<arr[mid+1]:
            start = mid
        elif arr[mid]<arr[mid-1]:
            end = mid
        else:
            start+=1


    return -1


if __name__ == "__main__":
    print(findPeak([1,2,3,1]))
    print(findPeak([1,2,1,3,5,6,4]))
    print(findPeak_Optimized([1, 2, 3, 1]))
    print(findPeak_Optimized([1,2,1,3,5,6,4]))
