class Solution:
    def maxProduct(self, a: List[int]) -> int:
        maxi=-sys.maxsize
        prefix=suffix=1
        for i in range(len(a)):
            prefix*=a[i]
            maxi=max(maxi,prefix)
            if a[i]==0:
                maxi=max(0,maxi)
                prefix=1
        for i in range(len(a)-1,-1,-1):
            suffix*=a[i]
            maxi=max(maxi,suffix)
            if a[i]==0:
                maxi=max(0,maxi)
                suffix=1
        return maxi