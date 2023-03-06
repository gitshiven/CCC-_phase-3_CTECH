#This Solution by CHATGPT 100% run rate
n = int(input())
gas = list(map(int, input().split()))
cost = list(map(int, input().split()))

tank = 0  # current amount of gas in the tank
start = 0  # starting station index
total_gas = 0  # total amount of gas we've accumulated
total_cost = 0  # total cost of traveling so far

for i in range(n):
    tank += gas[i] - cost[i]  # fill up the tank at the current station
    total_gas += gas[i]
    total_cost += cost[i]
    if tank < 0:  # if we run out of gas before reaching the next station
        start = i + 1  # we can't start from any previous station
        tank = 0  # start with an empty tank at the next station

# we can complete the circuit if the total amount of gas is greater than or equal to the total cost of traveling
if total_gas >= total_cost:
    print(start)
else:
    print(-1)
