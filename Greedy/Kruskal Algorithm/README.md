# Kruskal's Algorithm for Minimum Spanning Tree Problem

The Minimum Spanning Tree (MST) problem is a classic optimization problem in computer science. Given an undirected and weighted graph, the goal is to find a subgraph that connects all vertices and has the minimum possible total weight.

Kruskal's Algorithm is another well-known algorithm for finding the minimum spanning tree of a given graph. The algorithm starts with an empty set of edges and repeatedly adds the minimum-weight edge that does not create a cycle until all vertices are visited.

For example, if we have a graph represented as a dictionary where the keys are the vertices and the values are lists of tuples representing the edges and their weights:

```
{
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('C', 7), ('D', 9)]
}
```

We want to find the minimum spanning tree of this graph, which consists of the edges `AB`, `BC`, `BE`, and `AD`.

## Greedy Approach

One common approach to solving the MST problem using Kruskal's Algorithm is the greedy approach. In this approach, we start with an empty set of edges and repeatedly add the minimum-weight edge that does not create a cycle until all vertices are visited.

To keep track of the edges and avoid cycles, we create a sorted list of all edges and initialize a parent dictionary for each vertex in the graph. We then loop through all edges and add them to the minimum spanning tree if they don't create a cycle.

To check for cycles, we use the `find()` function to find the roots of the vertices and compare them. If they are not equal, we add the edge to the minimum spanning tree and update the parent dictionary.

Note that while the greedy approach may not always give us the optimal solution, it works well for many instances of the MST problem and is often efficient.

## Implementation

The implementation provided above uses a greedy approach to solve the MST problem using Kruskal's Algorithm. The function `kruskal_mst()` takes a dictionary `graph` as input, where the keys are the vertices and the values are lists of tuples representing the edges and their weights. The function returns a list of tuples representing the edges in the minimum spanning tree and their weights.

We first create a list of all edges sorted by weight. We then initialize the parent dictionary for each vertex in the graph.

We loop through all edges and add them to the minimum spanning tree if they don't create a cycle. To check for cycles, we use the `find()` function to find the roots of the vertices and compare them. If they are not equal, we add the edge to the minimum spanning tree and update the parent dictionary.

Note that this implementation assumes that the input graph is connected.

## Example Usage

Here's an example usage of the `kruskal_mst()` function:

```python
graph = {
    'A': [('B', 2), ('D', 6)],
    'B': [('A', 2), ('C', 3), ('D', 8), ('E', 5)],
    'C': [('B', 3), ('E', 7)],
    'D': [('A', 6), ('B', 8), ('E', 9)],
    'E': [('B', 5), ('C', 7), ('D', 9)]
}
mst = kruskal_mst(graph)
print(mst) # Output: [('A', 'B', 2), ('B', 'C', 3), ('B', 'E', 5), ('A', 'D', 6)]
```

In this example, we have a graph represented as a dictionary where the keys are the vertices and the values are lists of tuples representing the edges and their weights. The function returns a list of tuples representing the edges in the minimum spanning tree and their weights.