class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        i=0
        res=0
        for j in range(n):
            while nums[j]>nums[i]*k:
                i+=1
            res=max(res,j-i+1)
        return n-res