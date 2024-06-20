import random


def contracrion(vertices_list: list, edges_list: list) -> int:
    # edges_list = edges[:]
    # vertices_list = vertices[:]
    while len(vertices_list) > 2:
        vertice_1 = random.choice(vertices_list)
        vertice_2 = random.choice(edges_list[vertice_1 - 1])
        for i in edges_list[vertice_2 - 1]:
            if i != vertice_1:
                edges_list[vertice_1 - 1].append(i)
                index = edges_list[i - 1].index(vertice_2)
                edges_list[i - 1][index] = vertice_1
            else:
                index = index = edges_list[vertice_1 - 1].index(vertice_2)
                edges_list[vertice_1 - 1].pop(index)
        vertices_list.pop(vertices_list.index(vertice_2))
    result = [edges_list[vertices_list[0] - 1], edges_list[vertices_list[1] - 1]]
    return len(result[0])


file = open('graph.txt', 'r')
vertices = []
edges = []
for i in file:
    line = list(map(int, i.split()))
    edges.append(line[1:])
    vert = int(i.split()[0])
    vertices.append(vert)

# # print(vertices)
# vertices = [1, 2, 3, 4, 5, 6]
# edges = [[2, 3, 5, 6], [1, 3, 4], [1, 2, 5], [2, 5], [1, 3, 4], [1]]

n = len(edges)
result = []
for i in range(n):
    file = open('graph.txt', 'r')
    vertices = []
    edges = []
    for i in file:
        line = list(map(int, i.split()))
        edges.append(line[1:])
        vert = int(i.split()[0])
        vertices.append(vert)
    x = contracrion(vertices, edges)
    result.append(x)
print(min(result))
