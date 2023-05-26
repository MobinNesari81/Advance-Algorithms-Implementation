import heapq

def prim_mst(graph):
    """
    A function to find the minimum spanning tree of a given graph using Prim's algorithm with a greedy approach.
    
    :param graph: a dictionary representing the graph where the keys are the vertices and the values are lists of tuples representing the edges and their weights
    :return: a list of tuples representing the edges in the minimum spanning tree and their weights
    """
    # initialize the starting vertex and the visited set
    start_vertex = next(iter(graph))
    visited = {start_vertex}
    
    # create a priority queue of (weight, vertex1, vertex2) pairs where vertex1 is in visited and vertex2 is not
    pq = [(weight, start_vertex, vertex2) for vertex2, weight in graph[start_vertex]]
    heapq.heapify(pq)
    
    # loop until all vertices have been visited or there are no more edges left
    mst = []
    while pq and len(visited) < len(graph):
        weight, vertex1, vertex2 = heapq.heappop(pq)
        if vertex2 not in visited:
            visited.add(vertex2)
            mst.append((vertex1, vertex2, weight))
            for vertex3, weight2 in graph[vertex2]:
                if vertex3 not in visited:
                    heapq.heappush(pq, (weight2, vertex2, vertex3))
                    
    return mst
