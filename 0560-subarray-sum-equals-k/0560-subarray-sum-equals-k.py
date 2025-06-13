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
            if summ-k in brr:
                count+=brr[summ-k]
            if summ in brr:
                brr[summ]+=1
            else:
                brr[summ]=1
        return count