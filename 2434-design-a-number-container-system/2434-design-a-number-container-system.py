import heapq

class NumberContainers:
    def __init__(self):
        self.index_find_heap = {}  # Maps number -> min-heap of indices
        self.num_find = {}  # Maps index -> number

    def change(self, index: int, number: int) -> None:
        if index in self.num_find:
            old_num = self.num_find[index]
            if old_num in self.index_find_heap:
                heapq.heappush(self.index_find_heap[old_num], float('inf'))  # Lazy removal

        self.num_find[index] = number
        if number not in self.index_find_heap:
            self.index_find_heap[number] = []
        heapq.heappush(self.index_find_heap[number], index)

    def find(self, number: int) -> int:
        if number not in self.index_find_heap:
            return -1
        
        # Remove outdated indices
        while self.index_find_heap[number] and (
            self.index_find_heap[number][0] not in self.num_find 
            or self.num_find[self.index_find_heap[number][0]] != number
        ):
            heapq.heappop(self.index_find_heap[number])    

        return self.index_find_heap[number][0] if self.index_find_heap[number] else -1
