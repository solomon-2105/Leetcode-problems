class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini=nums[0]
        maxdiff=-1
        for i in range(1,len(nums)):
            if nums[i]>mini:
                maxdiff=max(maxdiff,nums[i]-mini)
            else:
                mini=nums[i]
        return maxdiff
