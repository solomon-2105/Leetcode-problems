class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        s , o = set() , 0
        for i in range(len(nums)):
            if nums[i] != target[i]:
                if nums[i] not in s:
                    s.add(nums[i])
                    o += 1
        return o