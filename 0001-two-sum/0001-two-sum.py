class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        a={}
        for i in range(len(nums)):
            comp=target-nums[i]
            if comp in a:
                return [i,a[comp]]
            a[nums[i]]=i
        return [-1,-1]