class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1
        summ=0
        for i,j in a.items():
            if j%k==0:
                summ+=i*j
        return summ