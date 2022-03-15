graph_1 = [[0 for _ in range(5)] for _ in range(5)]
graph_2 = [[0]*(5) for _ in range(5)]

graph_1[1][1] = 99
graph_2[1][1] = 88

print(graph_1)
print(graph_2)