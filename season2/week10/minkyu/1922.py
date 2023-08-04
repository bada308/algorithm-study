import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
    node1, node2, cost = map(int, input().split())
    heapq.heappush(graph[node1], (cost, node2))
    heapq.heappush(graph[node2], (cost, node1))

node_list = [1]
visited[1] = True
total_cost = 0

while node_list:
    node_list = []
    for i in range(len(visited)):
        del_list = []
        if visited[i]:
            for j in range(len(graph[i])):
                cost, node = graph[i][j]
                if not visited[node]:
                    heapq.heappush(node_list, (cost, node))
                else:
                    del_list.append((cost, node))
            for j in range(len(del_list)):
                graph[i].remove(del_list[j])

    for i in range(len(node_list)):
        cost, node = node_list[i]
        if not visited[node]:
            total_cost += cost
            node_list = [node]
            visited[node] = True
            break

print(total_cost)
"""
시간 초과로 틀리는데 풀고 싶어서 나중에 풀어볼게요...
6%에서 시간초과....

그나마 시간복잡도 더 줄인 코드
import sys
input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
    node1, node2, cost = map(int, input().split())
    graph[node1].append((cost, node2))
    graph[node2].append((cost, node1))

node_list = 1
visited[1] = True
total_cost = 0
visited_list = [1]
while node_list:
    node_list = 0
    min_cost = INF
    for i in visited_list:
        for j in range(len(graph[i])):
            cost, node = graph[i][j]
            if not visited[node]:
                if cost < min_cost:
                    min_cost = cost
                    node_list = node

    if node_list and min_cost != INF:
        total_cost += min_cost
        visited[node_list] = True
        visited_list.append(node_list)
    else:
        break

print(total_cost)
"""