# Travelling Salesperson Problem using Branch and Bound (User Input)

import math

# Functions to find minimum edges
def first_min(adj, i):
    min_val = math.inf
    for k in range(len(adj)):
        if i != k and adj[i][k] < min_val:
            min_val = adj[i][k]
    return min_val


def second_min(adj, i):
    first, second = math.inf, math.inf
    for j in range(len(adj)):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]
        elif adj[i][j] < second:
            second = adj[i][j]
    return second


# Branch and Bound function
def tsp_bb(adj, curr_bound, curr_weight, level, curr_path, visited):
    global final_res, final_path
    n = len(adj)

    if level == n:
        if adj[curr_path[level - 1]][curr_path[0]] != 0:
            curr_res = curr_weight + adj[curr_path[level - 1]][curr_path[0]]
            if curr_res < final_res:
                final_path = curr_path[:]
                final_path.append(curr_path[0])
                final_res = curr_res
        return

    for i in range(n):
        if adj[curr_path[level - 1]][i] != 0 and not visited[i]:
            temp_bound = curr_bound
            temp_weight = curr_weight + adj[curr_path[level - 1]][i]

            if level == 1:
                curr_bound -= (first_min(adj, curr_path[level - 1]) +
                               first_min(adj, i)) / 2
            else:
                curr_bound -= (second_min(adj, curr_path[level - 1]) +
                               first_min(adj, i)) / 2

            if curr_bound + temp_weight < final_res:
                curr_path[level] = i
                visited[i] = True

                tsp_bb(adj, curr_bound, temp_weight, level + 1, curr_path, visited)

            # Backtrack
            curr_bound = temp_bound
            visited[i] = False


# Main function
def solve_tsp(adj):
    global final_res, final_path
    n = len(adj)

    curr_bound = 0
    curr_path = [-1] * (n + 1)
    visited = [False] * n

    # Calculate initial bound
    for i in range(n):
        curr_bound += (first_min(adj, i) + second_min(adj, i))

    curr_bound = math.ceil(curr_bound / 2)

    # Start from city 0
    visited[0] = True
    curr_path[0] = 0

    tsp_bb(adj, curr_bound, 0, 1, curr_path, visited)

    print("\nMinimum cost:", final_res)
    print("Path:", final_path)


# -----------------------------
# User Input Section
# -----------------------------
n = int(input("Enter number of cities: "))

print("Enter adjacency matrix row by row:")
adj = []
for i in range(n):
    row = list(map(int, input().split()))
    adj.append(row)

final_res = math.inf
final_path = []

# Solve
solve_tsp(adj)