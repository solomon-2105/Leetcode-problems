class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        incr,decr,mal=1,1,1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                incr+=1
                decr=1
            elif nums[i]<nums[i-1]:
                decr+=1
                incr=1
            else:
                incr=1
                decr=1
            mal=max(mal,incr,decr)
        return mal