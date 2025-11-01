class Solution:
    def generateTag(self, c: str) -> str:
        res='#'
        j=0
        while j<len(c) and c[j]==" ":
            j+=1
        c=c[j:]
        for i in range(len(c)):
            if len(res)>=100:
                return res
            if c[i]==' ':
                continue
            if i==0:
                res+=c[i].lower()
            elif c[i-1]==' ':
                res+=c[i].upper()
            else:
                res+=c[i].lower()
        return res