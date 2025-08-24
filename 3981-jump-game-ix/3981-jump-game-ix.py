class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        brr=len(nums)
        a=[0]*brr #prefix
        b=[0]*brr #suffix
        a[0],b[-1]=nums[0],nums[-1]
        for i in range(1, brr):
            a[i]=max(a[i-1],nums[i])
        for i in range(brr-2,-1,-1):
            b[i]=min(b[i+1],nums[i])
        grr=a[:] #result
        for i in range(brr-2,-1,-1):
             if b[i+1]<a[i]:
                grr[i]=grr[i+1]
        return grr