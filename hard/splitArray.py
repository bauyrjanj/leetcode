def splitArray(nums, m):
    if m>len(nums) or m<0:
        return -1

    if m==len(nums):
        return max(nums)

    def isPossible(s):
        split = curr_sum = 0
        for num in nums:
            curr_sum+=num
            if curr_sum>s:
                split+=1
                curr_sum=num
                if split>m-1:
                    return False
        return True

    l = max(nums)
    h = sum(nums)
    while l<h:
        mid = (h + l) // 2
        if isPossible(mid):
            h = mid
        else:
            l = mid+1

    return l

if __name__=="__main__":
    print(splitArray([7, 2, 5, 10, 8], 2))
    print(splitArray([1, 2, 3, 4, 5], 2))
    print(splitArray([1,4,4], 3))

