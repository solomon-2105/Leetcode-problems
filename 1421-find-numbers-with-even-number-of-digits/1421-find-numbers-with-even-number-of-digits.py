class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            sum=0
            while i:
                sum+=1
                i//=10
            if sum%2==0: count+=1
        return count