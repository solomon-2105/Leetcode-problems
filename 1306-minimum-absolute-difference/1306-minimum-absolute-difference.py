class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        brr=float('inf')
        res=[]
        for i in range(len(arr)-1):
            grr=arr[i+1]-arr[i]
            if grr<brr:
                brr=grr
                res=[[arr[i], arr[i+1]]]
            elif grr==brr:
                res.append([arr[i], arr[i+1]])
        return res
