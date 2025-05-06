import sys

N = 4

graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

dp = [[-1] * (1 << N) for _ in range(N)]

def tsp(pos, visited):
    if visited == (1 << N) - 1:
        return graph[pos][0]

    if dp[pos][visited] != -1:
        return dp[pos][visited]

    ans = sys.maxsize
    for city in range(N):
        if visited & (1 << city) == 0:
            ans = min(ans, graph[pos][city] + tsp(city, visited | (1 << city)))

    dp[pos][visited] = ans
    return ans

min_cost = tsp(0, 1 << 0)
print("Minimum cost of TSP tour:", min_cost)
