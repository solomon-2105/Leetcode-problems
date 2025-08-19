class Solution(object):
    def maximumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a={}
        max_count=-1
        for i in nums:
            dig_sum=sum(int(j) for j in str(i))

            if dig_sum in a:
                max_count=max(max_count,a[dig_sum]+i)
                a[dig_sum]=max(a[dig_sum],i)
            else:
                a[dig_sum]=i
        return max_count