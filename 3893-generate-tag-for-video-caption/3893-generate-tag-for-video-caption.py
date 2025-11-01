class Solution:
    def generateTag(self, c: str) -> str:
        res='#'
        j=0
        while j<len(c) and c[j]==' ':
            j+=1
        i=j
        while i<len(c):
            if len(res)>=100:
                return res
            if c[i]==' ':
                i+=1
                continue
            if i==j:
                res+=c[i].lower()
            elif c[i-1]==' ':
                res+=c[i].upper()
            else:
                res+=c[i].lower()
            i+=1
        return res