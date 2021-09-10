#3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.
import random
def create_graph(vertex, percent=1.0):
    assert 0 < percent <= 1, 'неверный диапазон'
    graph = []
    for i in range(vertex):
        graph.append(set())
        count_edge = random.randrange(1, int(vertex*percent))
        while len(graph[i]) < count_edge:
            edge = random.randrange(0, vertex)
            if edge != i:
                graph[i].add(edge)
    return graph

def dfs(graph, start):
    path = []
    parent = [None for _ in range(len(graph))]
    is_visited = [False for _ in range(len(graph))]
    def _dfs(vertex):
        is_visited[vertex] = True
        path.append(vertex)

        for item in graph[vertex]:
            if not is_visited[item]:
                parent[item] = vertex
                _dfs(item)
                path.append(vertex)
            else:
                path.append(-vertex)
    _dfs(start)
    return parent, path

q = create_graph(int(input('количество вершин')),
                 float(input('процент от числа вершин')),
                 )

i = 0
for value in q:
    print(f'из вершины {i} ребра идут к вершинам {value}')
    i = i + 1
while True:
    s = int(input('\nначало (-1 для выхода)'))
    if s ==-1:
        break
    parent, path = dfs(q, s)
    print(parent)

    for i, vertex in enumerate(path):
        if i % 10 == 0:
            print()
print(vertex)
