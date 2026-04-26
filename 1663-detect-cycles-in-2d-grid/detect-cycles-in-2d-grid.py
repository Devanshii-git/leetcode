class Solution:
    def containsCycle(self, grid):
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(x, y, px, py):
            visited[x][y] = True
            
            directions = [(0,1), (1,0), (0,-1), (-1,0)]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                # Boundary check
                if nx < 0 or ny < 0 or nx >= rows or ny >= cols:
                    continue
                
                # Only move to same character
                if grid[nx][ny] != grid[x][y]:
                    continue
                
                if not visited[nx][ny]:
                    if dfs(nx, ny, x, y):
                        return True
                elif (nx, ny) != (px, py):
                    # Visited and not parent → cycle found
                    return True
            
            return False

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    if dfs(i, j, -1, -1):
                        return True
        
        return False