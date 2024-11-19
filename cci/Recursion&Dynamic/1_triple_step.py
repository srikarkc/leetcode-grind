def triple_step_recursive(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return (triple_step_recursive(n - 1) + triple_step_recursive(n - 2) + triple_step_recursive(n - 3))

# with memoization (dynamic programming)
def triple_step_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in memo:
        return memo[n]
    memo[n] = (triple_step_memo(n - 1, memo) +
               triple_step_memo(n - 2, memo) +
               triple_step_memo(n - 3, memo))
    return memo[n]


# use table to store result
def triple_step_dp(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 1, 1, 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    return dp[n]