class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        left = 0
        right = n * len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_row = mid // n
            mid_col = mid % n

            if target > matrix[mid_row][mid_col]:
                left =  mid + 1
            elif target < matrix[mid_row][mid_col]:
                right = mid - 1
            else:
                return True
        
        return False