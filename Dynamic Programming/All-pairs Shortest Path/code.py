def floyd_warshall(graph):
    # Create a copy of the graph so we can modify it without affecting the original
    graph = dict(graph)
    
    # Add missing edges with infinite weight
    for node1 in graph:
        for node2 in graph:
            if node1 != node2 and node2 not in graph[node1]:
                graph[node1][node2] = float('inf')
    
    # Compute shortest paths using dynamic programming
    for intermediate_node in graph:
        for start_node in graph:
            for end_node in graph:
                new_distance = graph[start_node][intermediate_node] + graph[intermediate_node][end_node]
                if new_distance < graph[start_node][end_node]:
                    graph[start_node][end_node] = new_distance
    
    return graph
