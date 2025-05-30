class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        d={}
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                p=nums[i]*nums[j]
                if p in d:
                    d[p]+=1
                else:
                    d[p]=1
        for key,value in d.items():
            if value>1:
                count=count+ (value*(value-1))//2
        return 8*int(count)