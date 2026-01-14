class Solution:
    def replaceElements(self, a: List[int]) -> List[int]:
        maxi = -1
        n = len(a)
        for i in range(n-1,-1,-1):
            cur = a[i]
            a[i] = maxi
            if cur > maxi:
                maxi = cur
        return a