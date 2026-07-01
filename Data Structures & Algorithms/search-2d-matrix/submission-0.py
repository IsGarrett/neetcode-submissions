class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = rows * cols -1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // cols, mid % cols
            guess = matrix[row][col]
            if guess == target:
                return True
            elif guess > target:
                right = mid - 1
            else:
                left = mid + 1
        return False
