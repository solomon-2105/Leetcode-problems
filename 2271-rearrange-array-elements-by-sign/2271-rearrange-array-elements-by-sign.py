class Solution:
    def rearrangeArray(self, bitch: List[int]) -> List[int]:
        pussy,nigga=0,1
        ass=[0]*len(bitch)
        for i in bitch:
            if i>0:
                ass[pussy]=i
                pussy+=2
            elif i<0:
                ass[nigga]=i
                nigga+=2
        return ass