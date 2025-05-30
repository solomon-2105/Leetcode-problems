class Solution:
    def minDominoRotations(self, tops: list[int], bottoms: list[int]) -> int:
        def check(x):
            top_rotations=0
            bottom_rotations=0
            for i in range(len(tops)):
                if tops[i]!=x and bottoms[i]!=x:
                    return float('inf')
                elif tops[i]!=x:
                    top_rotations+=1
                elif bottoms[i]!=x:
                    bottom_rotations+=1
            return min(top_rotations,bottom_rotations)

        rotations=min(check(tops[0]),check(bottoms[0]))
        return -1 if rotations==float('inf') else rotations
