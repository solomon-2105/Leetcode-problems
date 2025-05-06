class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n=len(arr)
        i=0
        while i<n:
            if arr[i]==0:
                arr.pop()
                arr.insert(i,0)
                i+=2
            else:
                i+=1
