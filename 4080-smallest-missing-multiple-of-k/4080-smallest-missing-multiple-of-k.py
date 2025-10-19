class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=set()
        for i in nums:
            a.add(i)
        i=1
        while True:
            c=k*i
            if c not in a:
                return c
            i+=1