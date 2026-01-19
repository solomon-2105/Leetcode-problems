class Solution:
    def reversePairs(self, a: List[int] ) -> int:
        self.count = 0
        self.merge_sort(a, 0, len(a) - 1)
        return self.count

    def merge_sort(self,a, l, r):
        if l < r:
            m = l + (r - l) // 2
            self.merge_sort(a, l, m)
            self.merge_sort(a, m + 1, r)
            self.reverse_pair(a,l,m,r)
            self.merge(a, l, m, r)

    def merge(self,a, l, m, r):
        temp = []
        left = l
        right = m + 1

        while left <= m and right <= r:
            if a[left] <= a[right]:
                temp.append(a[left])
                left += 1
            else:
                temp.append(a[right])
                right += 1

        while left <= m:
            temp.append(a[left])
            left += 1

        while right <= r:
            temp.append(a[right])
            right += 1

        for i in range(len(temp)):
            a[l + i] = temp[i]

    def reverse_pair(self,a,l,m,h):
        r = m + 1
        for i in range(l,m+1):
            while r <= h and a[i] > 2 * a[r] : r += 1
            self.count += (r - (m+1))