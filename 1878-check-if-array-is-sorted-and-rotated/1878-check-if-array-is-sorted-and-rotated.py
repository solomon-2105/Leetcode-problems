class Solution:
    def check(self, nums: List[int]) -> bool:
        c=0
        a=len(nums)
        for i in range(a):
            if nums[i]>nums[(i+1)%a]:
                c+=1
        if c<=1:
            return True
        return False