class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            a[i]=a.get(i,0)+1
        maxi=max(a.values())
        su=0
        for i,j in a.items():
            if j==maxi:
                su+=j
        return su