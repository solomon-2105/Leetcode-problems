class Solution:
    def reverseWords(self, s: str) -> str:
        def reversee(brr,left,right):
            while left<=right:
                brr[left],brr[right]=brr[right],brr[left]
                left+=1
                right-=1
        brr=list(s.strip())
        reversee(brr,0,len(brr)-1)
        i=k=0
        res=[]
        while k<len(brr):
            if brr[k]!=" ":
                k+=1
            else:
                reversee(brr,i,k-1)
                res.append("".join(brr[i:k]))
                while k<len(brr) and brr[k]==" ":
                    k+=1
                i=k
        reversee(brr,i,len(brr)-1)
        res.append("".join(brr[i:]))
        return " ".join(res)
