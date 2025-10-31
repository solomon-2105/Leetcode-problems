class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        a=set()
        c,d=0,0
        for i in nums:
            if i in a:
                if c==0:
                    c=i
                else:
                    d=i
            else:
                a.add(i)
        return [c,d]