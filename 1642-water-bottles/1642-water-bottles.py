class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk=0
        empty=0
        while True:
            total_drunk += numBottles
            empty += numBottles 
            numBottles = empty // numExchange 
            empty = empty % numExchange
            if numBottles == 0:
                total_drunk+=numBottles
                break
        return total_drunk