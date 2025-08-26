class Solution:
    def largestPerimeter(self, a: List[int]) -> int:
        a.sort()
        for i in range(len(a)-1,1,-1):
            if a[i]<a[i-1]+a[i-2]:
                return a[i]+a[i-1]+a[i-2]
        return 0