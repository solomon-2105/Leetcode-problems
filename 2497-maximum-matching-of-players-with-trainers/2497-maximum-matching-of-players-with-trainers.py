class Solution:
    def matchPlayersAndTrainers(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j=0,0
        count=0
        a,b=len(g),len(s)
        while i<a and j<b:
            if g[i]<=s[j]:
                i+=1
                j+=1
                count+=1
            else:
                j+=1
        return count 