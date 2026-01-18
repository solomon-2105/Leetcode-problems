class Solution:
    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        cx , cy = center
        qual = -1
        coord = [-1,-1]
        for x, y , q in towers:
            if abs(x-cx) + abs(y-cy) <= radius :
                if q > qual:
                    qual = q
                    coord = [x,y]
                elif q == qual:
                    if coord == None or [x,y] < coord :
                        coord = [x,y]
        return coord