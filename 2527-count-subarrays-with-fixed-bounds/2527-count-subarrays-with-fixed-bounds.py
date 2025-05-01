class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res=0
        min_pos=max_pos=bad=-1
        for i,x in enumerate(nums):
            if x<minK or x>maxK:
                bad=i
            if x==minK:
                min_pos=i
            if x==maxK:
                max_pos=i
            res+=max(0,min(min_pos,max_pos)-bad)
        return res
