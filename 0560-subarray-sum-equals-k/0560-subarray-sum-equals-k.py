class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        summ=0
        brr={0:1}
        for i in range(len(nums)):
            summ+=nums[i]
            rem=summ-k
            count+=brr.get(rem,0)
            brr[summ]= brr.get(summ,0)+1 
        return count