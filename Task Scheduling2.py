def max_profit(tasks):
    # Sort tasks by decreasing order of profit
    tasks = sorted(tasks, key=lambda x: x[1], reverse=True)
    n = len(tasks)
    # Initialize a set to keep track of the deadlines that are already used
    used = set()
    total_profit = 0
    for i in range(n):
        deadline, profit = tasks[i]
        # Try to find the nearest unused deadline for the current task
        j = deadline
        while j > 0 and j in used:
            j -= 1
        # If a deadline is found, add the current task to the schedule and update the used set
        if j > 0:
            used.add(j)
            total_profit += profit
    return total_profit


# Read the number of test cases
t = int(input())

# Process each test case
for i in range(t):
    # Read the input for the current test case
    n = int(input())
    t_vals = list(map(int, input().split()))
    p_vals = list(map(int, input().split()))
    tasks = [(t_vals[j], p_vals[j]) for j in range(n)]
    # Compute the maximum profit for the current test case and print the result
    result = max_profit(tasks)
    print(result)
