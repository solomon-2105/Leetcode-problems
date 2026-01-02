class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        # n = len(nums) // 2
        # a = {}
        # for i in nums :
        #     a[i] = a.get( i , 0 ) + 1
        # for i , j in a.items() :
        #     if j == n :
        #         return i
        for i in range ( len(nums) - 2 ) :
            if nums[i] == nums[i+1] or nums[i] == nums[i+2] :
                return nums[i]
        return nums[-1]