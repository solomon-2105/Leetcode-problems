class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            idx=abs(nums[i])-1
            if nums[idx]<0:
                a.append(idx+1)
            else:
                nums[idx]*=-1
        return a