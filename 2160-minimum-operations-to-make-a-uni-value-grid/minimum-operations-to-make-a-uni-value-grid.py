class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        
        arr = []
        
        # Flatten the grid
        for row in grid:
            for num in row:
                arr.append(num)
        
        # Check if all elements can be converted
        rem = arr[0] % x
        
        for num in arr:
            if num % x != rem:
                return -1
        
        # Sort and choose median
        arr.sort()
        median = arr[len(arr) // 2]
        
        # Calculate operations
        operations = 0
        
        for num in arr:
            operations += abs(num - median) // x
        
        return operations