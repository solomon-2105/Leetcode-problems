class Solution:
    def minCost(self, c: str, n: List[int]) -> int:
        prev=mintime=i=0
        while i<len(c):
            if i>0 and c[i]!=c[i-1]:
                prev=0 
            curr=n[i]
            mintime+=min(prev,curr)
            prev=max(prev,curr)
            i+=1
        return mintime
