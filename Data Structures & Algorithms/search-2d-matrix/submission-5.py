class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        maxRow = len(matrix)
        maxCol = len(matrix[0])

        top = 0
        bottom = maxRow - 1
        while top <= bottom:
            midRow = (top + bottom) // 2
            if matrix[midRow][-1] < target:
                top = midRow + 1
            elif matrix[midRow][0] > target:
                bottom = midRow - 1
            else: 
                break
        
        if not (top <= bottom):
            return False

        left = 0
        right = maxCol - 1
        finalRow = (top + bottom) // 2
        while left <= right:
            midCol = (left + right) // 2
            if matrix[finalRow][midCol] == target:
                return True
            elif matrix[finalRow][midCol] < target:
                left = midCol + 1
            else:
                right = midCol - 1

        return False
            
        