class Solution:
    def maxDifference(self, s: str) -> int:
        # brr=[0]*26
        mini,maxi=len(s),0
        # for  i in s:
        #     brr[ord(i)-ord('a')]+=1
        # for i in range(26):
        #     if (brr[i]%2)!=0:
        #         maxi=max(maxi,brr[i])
        #     if (brr[i]%2)==0 and brr[i]>0:
        #         mini=min(mini,brr[i])
        # return maxi-mini

        brr={}
        for i in s:
            brr[i]=brr.get(i,0)+1
        for i,j in brr.items():
            if (j%2)!=0:
                maxi=max(maxi,j)
            if (j%2)==0 and j>0:
                mini=min(mini,j)
        return maxi-mini