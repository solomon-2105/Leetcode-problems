class Solution:
    def subarraySum(self, brr: List[int], k: int) -> int:
        drr={}
        drr[0]=1
        prr=0
        crr=0
        for i in range(len(brr)):
            prr+=brr[i]
            rem=prr-k
            if rem in drr:
                crr+=drr[rem]
            if prr in drr:
                drr[prr]+=1
            else:
                drr[prr]=1
        return crr
