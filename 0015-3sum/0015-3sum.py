class Solution:
    def threeSum(self, a: List[int]) -> List[List[int]]:
        # aaha=set() #bruteforce
        # for i in range(len(a)):
        #     for j in range(i+1,len(a)):
        #         for k in range(j+1,len(a)):
        #             if a[i]+a[j]+a[k]==0:
        #                 brr=[a[i],a[j],a[k]]
        #                 brr.sort()
        #                 aaha.add(tuple(brr))
        # d=[list(i) for i in aaha]
        # return d

        #better
        # drr=set()
        # for i in range(len(a)):
        #     brr=set()
        #     for j in range(i+1,len(a)):
        #         grr=-(a[i]+a[j])
        #         if grr in brr:
        #             drr.add(tuple(sorted([a[i],a[j],grr])))
        #         brr.add(a[j])
        # crr=[list(i) for i in drr]
        # return crr

        #two pointers (optimal)
        brr=list()
        a.sort()
        for i in range(len(a)):
            if i>0 and a[i]==a[i-1]: continue
            j=i+1
            k=len(a)-1
            while j<k:
                summ=a[i]+a[j]+a[k]
                if summ<0:
                    j+=1
                elif summ>0:
                    k-=1
                else:
                    ass=[a[i],a[j],a[k]]
                    brr.append(ass)
                    j+=1
                    k-=1
                    while j<k and a[j]==a[j-1]: j+=1
                    while j<k and a[k]==a[k+1]: k-=1
        return brr