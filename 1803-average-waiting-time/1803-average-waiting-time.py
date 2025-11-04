class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        n=len(customers)
        wait_time=current_time=0
        for arrival,cook in customers:
            current_time=max(current_time,arrival)+cook
            wait_time+=current_time-arrival
        return wait_time/n