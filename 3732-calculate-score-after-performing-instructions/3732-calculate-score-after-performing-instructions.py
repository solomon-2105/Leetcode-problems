class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n=len(values)
        a=set()
        i=0
        score=0
        while 0<=i<n:
            if i in a:#[0,2,3,4,5,]
                    return score
            a.add(i)
            if instructions[i]=="add": 
                score+=values[i]
                i+=1
            elif instructions[i]=="jump":
                i=i+values[i]
        return score







                    