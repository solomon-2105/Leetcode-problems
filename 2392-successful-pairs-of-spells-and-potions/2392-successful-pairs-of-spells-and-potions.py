class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res=[]
        i=0
        while i<len(spells):
            j=0
            l,h=0,len(potions)-1
            while l<=h:
                j=l+(h-l)//2
                mul=spells[i]*potions[j]
                if mul<success:
                    l=j+1
                else:
                    h=j-1
            res.append(len(potions)-l)
            i+=1
        return res