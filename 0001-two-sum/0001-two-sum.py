class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        b={}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in b:
                return [i,b[comp]]
            b[nums[i]]=i
        return -1