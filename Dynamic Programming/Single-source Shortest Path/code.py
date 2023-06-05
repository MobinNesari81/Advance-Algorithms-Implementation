import heapq

def dijkstra(graph, start):
    # Create a dictionary to store the shortest distances to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Create a priority queue of nodes to visit
    heap = []
    heapq.heappush(heap, (distances[start], start))
    
    # Visit each node in the graph
    visited = set()
    while heap:
        dist, node = heapq.heappop(heap)
        if node in visited:
            continue
        
        # Update the distances to neighboring nodes
        visited.add(node)
        for neighbor, weight in graph[node].items():
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return distances
