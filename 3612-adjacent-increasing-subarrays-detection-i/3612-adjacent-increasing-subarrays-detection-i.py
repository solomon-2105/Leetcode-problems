class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        i=0
        while i+2*k<=len(nums):
            if self.check(nums,i,k) and self.check(nums,i+k,k):
                    return True
            i+=1
        return False

    def check(self,nums,a,b):
        for i in range(a,a+b-1):
            if nums[i]>=nums[i+1]:
                return False
        return True