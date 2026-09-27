# 0/1 Knapsack using Top-Down Dynamic Programming

def knapsack(weights, values, n, capacity, table):

    # Base case
    if n == 0 or capacity == 0:
        return 0

    # Check if value is already calculated
    if table[n][capacity] != -1:
        return table[n][capacity]

    # If item is too heavy, skip it
    if weights[n - 1] > capacity:

        table[n][capacity] = knapsack(
            weights, values, n - 1, capacity, table
        )

    else:
        # Include the item
        include = values[n - 1] + knapsack(
            weights,
            values,
            n - 1,
            capacity - weights[n - 1],
            table
        )

        # Exclude the item
        exclude = knapsack(
            weights,
            values,
            n - 1,
            capacity,
            table
        )

        # Choose the maximum value
        table[n][capacity] = max(include, exclude)

    return table[n][capacity]


# Main Program

weights = [2, 1, 3, 2]
values = [12, 10, 20, 15]

capacity = 5
n = len(weights)

# Create table
table = [[-1 for _ in range(capacity + 1)]
         for _ in range(n + 1)]

maximum = knapsack(weights, values, n, capacity, table)

print("Maximum value using Top-Down:", maximum)