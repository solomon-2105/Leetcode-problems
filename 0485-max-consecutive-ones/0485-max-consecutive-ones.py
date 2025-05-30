class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum=0
        max_sum=0
        for i in nums:
            if i==1: 
                current_sum+=1
                max_sum=max(max_sum,current_sum)
            else:
                current_sum=0
        return max_sum



        