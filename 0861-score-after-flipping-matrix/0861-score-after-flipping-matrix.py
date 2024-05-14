class Solution:
    def matrixScore(self, grid):
        m, n = len(grid), len(grid[0])

        # Step 1: Toggle rows if the first element in each row is 0
        for i in range(m):
            if grid[i][0] == 0:
                for j in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # Step 2: Toggle columns if the number of 1s is less than half of total rows
        for j in range(1, n):
            count_ones = sum(grid[i][j] for i in range(m))
            if count_ones < m / 2:
                for i in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # Step 3: Calculate the score
        score = sum(int(''.join(map(str, row)), 2) for row in grid)
        return score

# Test cases
solution = Solution()
grid1 = [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
print(solution.matrixScore(grid1))  # Output: 39

grid2 = [[0]]
print(solution.matrixScore(grid2))  # Output: 1
