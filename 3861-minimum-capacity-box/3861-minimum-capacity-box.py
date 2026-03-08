class Solution:
    def minimumIndex(self, capacity: list[int], itemSize: int) -> int:
        minIndex = len(capacity)
        mini = 101
        for i in range(len(capacity)):
            if capacity[i] >= itemSize:
                if capacity[i] < mini:
                    minIndex = i
                    mini = capacity[i]
        return -1 if minIndex == len(capacity) else minIndex