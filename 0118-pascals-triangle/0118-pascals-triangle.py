class Solution:
    def generate(self, n: int) -> List[List[int]]:
        #combinatorics

        # grr=[]
        # for i in range(n):
        #     res=1
        #     brr=[1]
        #     for j in range(1,i+1):
        #         res*=(i-j+1)
        #         res//=j
        #         brr.append(res)
        #     grr.append(brr)
        # return grr


        #Dynamic programming
        a=[[1]*(i+1) for i in range(n)]
        for i in range(2,n):
            for j in range(1,i):
                a[i][j]=a[i-1][j-1]+a[i-1][j]
        return a