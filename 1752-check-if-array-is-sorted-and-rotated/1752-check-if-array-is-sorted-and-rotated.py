class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return True
        count = 1
        for i in range(len(nums)*2):
            if nums[(i-1) % n] <= nums[i % n]:
                count+=1
            else:
                count=1
            if count==n:
                return True
        return False