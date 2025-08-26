class Solution:
    def areaOfMaxDiagonal(self, a: List[List[int]]) -> int:
        grr=0
        brr=0
        for i in range(len(a)):
            l,w=a[i]
            d=(l**2+w**2)**0.5
            ar=l*w
            if d>grr:
                grr=d
                brr=ar
            elif d==grr:
                brr=max(brr,ar)
        return brr