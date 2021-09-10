#Доработать алгоритм Дейкстры (рассматривался на уроке),
# чтобы он дополнительно возвращал список вершин, которые необходимо обойти.
s = int(input('начальная вершина'))
q = [[0, 0, 1, 1, 5],
    [0, 0, 9, 4, 2],
    [0, 0, 1, 2, 3],
    ]
cost = 0
def bfs(graph, start):
    min_cost = 0
    cost = [float('inf')] * len(graph)
    parent = [-1] * len(graph)
#    cost(start) = 0
    while min_cost < float('inf'):
        is_visited = [bool(True)] * len(graph)
        for i, vertex in enumerate(graph[start]):
            if vertex == 1 and not is_visited[i]:
                if cost[i] > vertex + cost[start]:
                    cost[i] = vertex + cost[start]
                    parent[i] = start
                    min_cost = float('inf')
        for i in range(len(graph)):
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i
        result = [[] for _ in range(len(graph))]
        for i in range(len(graph)):
            if is_visited[i]:
                result[i].append(parent[i])
                j = 1
                while parent[j] != -1:
                    result[j].append(parent[j])
                    j = parent[j]
                result[i].reverse()
        return min_cost, cost, result


min_cost, path = bfs(q, s)
print(f'минимальный путь до вершины {min_cost}')
print(path, sep='\n')
