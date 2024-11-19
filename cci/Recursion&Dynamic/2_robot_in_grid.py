def robot_in_grid(r, c):
    if r == 0 or c == 0:
        return 1
    
    return robot_in_grid(r - 1, c) + robot_in_grid(r, c - 1)

rows, cols = 3, 3
print(robot_in_grid(rows - 1, cols - 1))  # Output: 6

def robot_in_grid_memo(r, c, memo=None):
    if memo is None:
        memo = {}
    # Base cases
    if r == 0 or c == 0:
        return 1
    # Check memo
    if (r, c) in memo:
        return memo[(r, c)]
    # Recursive calculation with memoization
    memo[(r, c)] = robot_in_grid_memo(r - 1, c, memo) + robot_in_grid_memo(r, c - 1, memo)
    return memo[(r, c)]

# Example
rows, cols = 3, 3
print(robot_in_grid_memo(rows - 1, cols - 1))  # Output: 6


def robot_in_grid_dp(rows, cols):
    # Initialize a dp table with all elements as 1
    dp = [[1] * cols for _ in range(rows)]

    # Fill the dp table
    for r in range(1, rows):
        for c in range(1, cols):
            dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[rows - 1][cols - 1]

# Example
rows, cols = 3, 3
print(robot_in_grid_dp(rows, cols))  # Output: 6


def robot_in_grid_with_obstacles(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the first row and column
    for r in range(rows):
        if grid[r][0] == 0:
            break
        dp[r][0] = 1

    for c in range(cols):
        if grid[0][c] == 0:
            break
        dp[0][c] = 1

    # Fill the dp table
    for r in range(1, rows):
        for c in range(1, cols):
            if grid[r][c] == 1:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]

    return dp[rows - 1][cols - 1]

# Example grid with obstacles
grid = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
print(robot_in_grid_with_obstacles(grid))  # Output: 2
