class Solution:
    def smallestAbsent(self, nums: List[int]) -> int:
        a=set(nums)
        brr=sum(nums)/len(nums)
        grr=floor(brr)+1
        while True:
            if grr not in a and grr>brr and grr>0:
                return grr
            grr+=1