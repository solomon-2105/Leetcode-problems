from bisect import bisect_left, bisect_right, insort
from sortedcontainers import SortedList

class Solution:
    def maxTaskAssign(self,tasks:List[int],workers:List[int],pills:int,strength:int)->int:
        tasks.sort()
        workers.sort()
        
        def can_assign(k):
            sl=SortedList(workers[-k:])
            p=pills
            for i in range(k-1,-1,-1):
                idx=sl.bisect_left(tasks[i])
                if idx<len(sl):
                    sl.pop(idx)
                else:
                    if p==0:
                        return False
                    idx=sl.bisect_left(tasks[i]-strength)
                    if idx==len(sl):
                        return False
                    sl.pop(idx)
                    p-=1
            return True
        
        l=0
        r=min(len(tasks),len(workers))
        res=0
        while l<=r:
            m=(l+r)//2
            if can_assign(m):
                res=m
                l=m+1
            else:
                r=m-1
        return res
