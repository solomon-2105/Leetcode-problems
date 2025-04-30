import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # count=0
        # for i in nums:
        #     sum=0
        #     while i:
        #         sum+=1
        #         i//=10
        #     if sum%2==0: count+=1
        # return count
        count=0
        for i in nums:
            a=int(math.log10(i)+1)
            if a%2==0: count+=1
        return count