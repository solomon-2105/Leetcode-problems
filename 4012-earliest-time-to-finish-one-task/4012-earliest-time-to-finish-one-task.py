class Solution:
    def earliestTime(self, tasks: List[List[int]]) -> int:
        maxi=float('inf')
        for i in range(len(tasks)):
            so=tasks[i][0]+tasks[i][1]
            maxi=min(maxi,so)
        return maxi
