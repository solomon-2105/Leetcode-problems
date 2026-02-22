class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        current_time = 0
        waiting_time = 0
        for i in range(n):
            current_time = max( current_time , customers[i][0]) + customers[i][1]
            waiting_time += current_time - customers[i][0]
        return waiting_time / n