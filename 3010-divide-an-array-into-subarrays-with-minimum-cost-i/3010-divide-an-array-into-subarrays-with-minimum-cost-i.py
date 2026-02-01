class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        sum = nums[0]
        first = second = float('inf')
        for i in range(1 , len(nums)):
            if nums[i] <= first:
                second = first
                first = nums[i]
            elif nums[i] < second:
                second = nums[i]
        return sum + first + second