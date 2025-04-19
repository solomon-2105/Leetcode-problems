class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Create a new matrix with transposed dimensions
        result = [[0] * rows for _ in range(cols)]
        
        # Fill the result matrix with transposed values
        for i in range(rows):
            for j in range(cols):
                result[j][i] = matrix[i][j]
                
        return result
