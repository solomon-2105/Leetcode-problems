class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        eve, odd=0,1
        a=len(nums)
        ans=[0]*a
        for i in range(a):
            if nums[i]%2==0:
                ans[eve]=nums[i]
                eve+=2
            elif nums[i]%2==1:
                ans[odd]=nums[i]
                odd+=2
        return ans