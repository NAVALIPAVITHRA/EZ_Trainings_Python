def solve(nums,n):
    cursum=nums[0]
    maxsum=nums[0]
    for num in nums[1:]:
        maxsum=max(num,maxsum+num)
        cursum=max(cursum,maxsum)
    return cursum
n=int(input())
arr=list(map(int,input().split()))
print(solve(arr,n))