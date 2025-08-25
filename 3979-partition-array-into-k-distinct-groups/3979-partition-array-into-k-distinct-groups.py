class Solution(object):
    def partitionArray(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums)%k !=0:
            return False
        else:
            bitch=len(nums)//k
            a={}
            for i in nums:
                a[i]=a.get(i,0)+1
            for w in a.values():
                if w>bitch: return False
            return True