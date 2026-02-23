class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n = len(customers)
        total_waiting_time = 0
        current_time = 0
        for arrival_time , cooking_time in customers:
            if current_time < arrival_time :
                current_time = arrival_time
            waiting_time = current_time + cooking_time - arrival_time
            total_waiting_time += waiting_time
            current_time += cooking_time
        return total_waiting_time / n