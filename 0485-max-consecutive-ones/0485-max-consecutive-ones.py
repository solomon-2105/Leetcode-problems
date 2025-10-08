class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=0
        maxi=0
        for i in nums:
            if i==1:
                count+=1
                maxi=max(count,maxi)
            else:
                count=0
        return maxi