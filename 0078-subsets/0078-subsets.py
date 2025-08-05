class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def brr(i,a,b,c):
            if i==len(a):
                c.append(b.copy())
                return
            b.append(a[i])
            brr(i+1,a,b,c)
            b.pop()
            brr(i+1,a,b,c)
        b,c=[],[]
        brr(0,nums,b,c)
        return c