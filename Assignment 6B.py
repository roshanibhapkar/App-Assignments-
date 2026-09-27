# 0/1 Knapsack using Bottom-Up Dynamic Programming

def knapsack(weights, values, capacity):

    n = len(weights)

    # Create DP table
    dp = [[0] * (capacity + 1) for i in range(n + 1)]

    # Fill the table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            if weights[i - 1] <= w:

                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Main program

weights = [2, 3, 4, 5]
values = [10, 20, 26, 36]
capacity = 7

result = knapsack(weights, values, capacity)

print("Maximum value:", result)