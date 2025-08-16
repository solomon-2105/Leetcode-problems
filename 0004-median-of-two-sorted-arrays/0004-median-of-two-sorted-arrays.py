class Solution:
    def findMedianSortedArrays(self, a: List[int], b: List[int]) -> float:
        c,d=len(a),len(b)
        if c>d:
            a,b=b,a
            c,d=d,c
        low,high=0,c
        while low<=high:
            mid1=low+(high-low)//2
            mid2=(c+d+1)//2-mid1
            
            l1=a[mid1-1] if mid1>0 else float('-inf')
            r1=a[mid1] if mid1<c else float('inf')
            l2=b[mid2-1] if mid2>0 else float('-inf')
            r2=b[mid2] if mid2<d else float('inf')

            if l1<=r2 and l2<=r1:
                if (c+d)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            elif l1>r2:
                high=mid1-1
            elif l2>r1:
                low=mid1+1