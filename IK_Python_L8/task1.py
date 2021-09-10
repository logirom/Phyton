#На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?
n = int(input('введите количество друзей  '))

def frends(num):
    graph = []
    for i in range(num):
        for j in range(num):
            if i !=j:
                graph.append((i, j))
    print(graph)
    return len(graph)//2

print(f"Всего было произведено {frends(n)} рукопожатий")
