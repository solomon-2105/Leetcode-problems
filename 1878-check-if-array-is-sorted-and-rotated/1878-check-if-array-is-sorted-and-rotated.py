class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count=0
        for i in range(len(nums)):
            if nums[i]>nums[(i+1)%len(nums)]:
                count+=1
        return count<=1