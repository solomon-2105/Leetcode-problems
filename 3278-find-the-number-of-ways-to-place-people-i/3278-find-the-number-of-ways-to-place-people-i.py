# class Solution:
#     def numberOfPairs(self, p: List[List[int]]) -> int:
#         #O(n^3) tc
#         count=0
#         for i in range(len(p)):
#             c,d=p[i]
#             for j in range(len(p)):
#                 if j!=i:
#                     a,b=p[j]
#                     if c<=a and d>=b:
#                         brr=True
#                         for k in range(len(p)):
#                             if k!=i and k!=j:
#                                 q,r=p[k]
#                                 if c<=q<=a and b<=r<=d:
#                                     brr=False
#                         if brr:count+=1
#         return count

class Solution:
    def numberOfPairs(self, p: List[List[int]]) -> int:
        p.sort(key=lambda x:(x[0],-x[1]))  # sort by x asc, y desc
        n=len(p)
        count=0
        for i in range(n):
            c,d=p[i]
            for j in range(i+1,n):
                a,b=p[j]
                if d>=b:  # A must be upperleft of B
                    brr=True
                    for k in range(i+1,j):  # only check points in between
                        q,r=p[k]
                        if c<=q<=a and b<=r<=d:
                            brr=False
                            break
                    if brr:count+=1
        return count

