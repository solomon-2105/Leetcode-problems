class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def find_median(a,b):
            c,d=len(a),len(b)
            total=c+d
            i=j=brr=0
            if total%2==0:
                mid1=total//2-1
                mid2=total//2
                val1=val2=None
                while i<c and j<d:
                    if a[i]<=b[j]:
                        if brr==mid1:
                            val1=a[i]
                        if brr==mid2:
                            val2=a[i]
                            return (val1+val2)/2
                        i+=1
                    else:
                        if brr==mid1:
                            val1=b[j]
                        if brr==mid2:
                            val2=b[j]
                            return (val1+val2)/2
                        j+=1
                    brr+=1
                while i<c:
                    if brr==mid1:
                        val1=a[i]
                    if brr==mid2:
                        val2=a[i]
                        return (val1+val2)/2
                    i+=1
                    brr+=1
                while j<d:
                    if brr==mid1:
                        val1=b[j]
                    if brr==mid2:
                        val2=b[j]
                        return (val1+val2)/2
                    j+=1
                    brr+=1
            else:
                mid=total//2
                while i<c and j<d:
                    if a[i]<=b[j]:
                        if brr==mid:
                            return a[i]
                        i+=1
                    else:
                        if brr==mid:
                            return b[j]
                        j+=1
                    brr+=1
                while i<c:
                    if brr==mid:
                        return a[i]
                    i+=1
                    brr+=1
                while j<d:
                    if brr==mid:
                        return b[j]
                    j+=1
                    brr+=1
        return find_median(nums1,nums2)
