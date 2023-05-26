def kruskal_mst(graph):
    """
    A function to find the minimum spanning tree of a given graph using Kruskal's algorithm with a greedy approach.
    
    :param graph: a dictionary representing the graph where the keys are the vertices and the values are lists of tuples representing the edges and their weights
    :return: a list of tuples representing the edges in the minimum spanning tree and their weights
    """
    # create a list of all edges sorted by weight
    edges = [(weight, vertex1, vertex2) for vertex1 in graph for vertex2, weight in graph[vertex1]]
    edges.sort()
    
    # initialize the parent dictionary for each vertex in the graph
    parent = {vertex: vertex for vertex in graph}
    
    # loop through all edges and add them to the minimum spanning tree if they don't create a cycle
    mst = []
    for weight, vertex1, vertex2 in edges:
        root1 = find(vertex1, parent)
        root2 = find(vertex2, parent)
        if root1 != root2:
            mst.append((vertex1, vertex2, weight))
            parent[root1] = root2
            
    return mst


def find(vertex, parent):
    """
    A helper function to find the root of a given vertex in the parent dictionary using path compression
    
    :param vertex: the vertex to find the root of
    :param parent: a dictionary representing the parent of each vertex in the graph
    :return: the root of the given vertex
    """
    while parent[vertex] != vertex:
        parent[vertex] = parent[parent[vertex]]
        vertex = parent[vertex]
    return vertex
