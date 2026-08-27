class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        length_m = len(matrix)
        length_n = len(matrix[0])

        row_start, column_start = 0, 0
        row_end, column_end = length_m - 1, length_n - 1

        if target < matrix[0][0] or target > matrix[row_end][column_end]:
            return False
        
        if target == matrix[0][0] or target == matrix[row_end][column_end]:
            return True

        row = 0
        
        # Find the row index of target
        while row_start <= row_end:
            row = (row_start + row_end) // 2
            if target > matrix[row][-1]:
                row_start = row + 1
            elif target < matrix[row][0]:
                row_end = row - 1
            else:
                break

        while column_start <= column_end:
            mid_j = (column_start + column_end) // 2
            if target > matrix[row][mid_j]:
                column_start = mid_j + 1
            elif target < matrix[row][mid_j]:
                column_end = mid_j - 1
            else:
                return True

        return False    
        
    

