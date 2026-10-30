
import heapq
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('A', 2), ('C', 1), ('D', 4)],
    'C': [('A', 3), ('B', 1), ('D', 5), ('E', 6)],
    'D': [('B', 4), ('C', 5), ('E', 2)],
    'E': [('C', 6), ('D', 2)]
}
def prim(graph, start):
    visited = set()
    min_heap = [(0, start, None)]
    total_cost = 0
    print("Minimum Spanning Tree:")
    while min_heap and len(visited) < len(graph):
        weight, vertex, parent = heapq.heappop(min_heap)
        if vertex in visited:
            continue
        visited.add(vertex)
        if parent is not None:
            print(parent, "-", vertex, ":", weight)
            total_cost += weight
        for neighbor, edge_weight in graph[vertex]:
            if neighbor not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbor, vertex)
                )
    if len(visited) != len(graph):
        print("Graph is disconnected.")
        return
    print("Total Minimum Cost:", total_cost)
prim(graph, 'A')
