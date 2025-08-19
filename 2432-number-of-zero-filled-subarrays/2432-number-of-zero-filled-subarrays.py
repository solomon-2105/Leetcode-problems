class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        i,j=0,0
        maxi,c=0,0
        while i<len(nums):
            if nums[i]==0:
                j=i
                while j<len(nums) and nums[j]==0:
                    j+=1
                c=(j-i)*(j-i+1)//2
                maxi+=c
                i=j
            else:
                i+=1
        return maxi