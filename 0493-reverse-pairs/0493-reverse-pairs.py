class Solution:
    def merge(self,a,low,mid,high):
        m=mid-low+1
        n=high-mid
        brr=[0]*m
        grr=[0]*n
        for i in range(m):
            brr[i]=a[low+i]
        for j in range(n):
            grr[j]=a[mid+j+1]
        i,j,huh=0,0,low
        while i<m and j<n:
            if brr[i]<=grr[j]:
                a[huh]=brr[i]
                i+=1
            else:
                a[huh]=grr[j]
                j+=1
            huh+=1
        while i<m:
            a[huh]=brr[i]
            i+=1
            huh+=1
        while j<n:
            a[huh]=grr[j]
            j+=1
            huh+=1

    def count_pairs(self,a,low,mid,high):
        right=mid+1
        for i in range(low,mid+1):
            while right<=high and a[i]>2*a[right]:
                right+=1
            self.count=self.count+(right-(mid+1))

    def merge_sort(self,a,low,high):
        if low<high:
            mid=low+(high-low)//2
            self.merge_sort(a,low,mid)
            self.merge_sort(a,mid+1,high)
            self.count_pairs(a,low,mid,high)
            self.merge(a,low,mid,high)

    def reversePairs(self,nums):
        self.count=0
        self.merge_sort(nums,0,len(nums)-1)
        return self.count
