class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],-x[0]))
        x=intervals[0][1]-1
        y = intervals[0][1]
        count=2
        for l,r in intervals[1:]:
            if l<=x:
                continue
            if l>x and l<=y:
                x=y
                y=r
                count+=1
                continue
            x=r-1
            y=r
            count+=2
        return count
