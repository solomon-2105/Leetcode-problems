class Solution:
    def merge(self, a: List[List[int]]) -> List[List[int]]:
        a.sort(key = lambda x : x[0])
        temp = []
        for i,j in a:
            if not temp or temp[-1][1]<i:
                temp.append([i,j])      
            else:
                temp[-1][1] = max(temp[-1][1] , j)
        return temp