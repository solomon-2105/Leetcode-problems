class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini,maxi=min(nums),max(nums)
        nums=set(nums)
        a=[]
        for i in range(mini,maxi+1):
            if i not in nums:
                a.append(i)
        return a