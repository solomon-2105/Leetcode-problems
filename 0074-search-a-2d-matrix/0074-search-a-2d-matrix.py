class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        c,d=len(a),len(a[0])
        low,high=0,c*d-1
        while low<=high:
            mid=low+(high-low)//2
            mid_val=a[mid//d][mid%d]
            if mid_val==target:
                return True
            elif mid_val<target: low=mid+1
            else : high=mid-1
        return False
