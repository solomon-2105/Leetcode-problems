class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        a=len(nums)
        for j in range(a):
            if nums[j]!=nums[i]:
                i+=1
                nums[i]=nums[j]
        return i+1