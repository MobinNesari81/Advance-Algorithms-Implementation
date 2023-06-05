# Single-Source Shortest Path with Dynamic Programming

This is a Python implementation of the single-source shortest path problem using dynamic programming and Dijkstra's algorithm. Given a weighted graph and a starting node, the goal is to find the shortest path from the start node to all other nodes in the graph.

## Dynamic Programming Approach

The key idea behind the dynamic programming approach to this problem is to build up a table of the shortest paths to each node in the graph. Specifically, we can define an array `distances` such that `distances[node]` represents the shortest distance from the start node to `node`. We can then fill in this array iteratively, starting with `distances[start] = 0` (since the distance from the start node to itself is 0) and working our way out to all other nodes.

To find the shortest path to a node `node`, we need to consider all possible paths from the start node to `node` and take the minimum of those distances. However, considering all possible paths would be prohibitively expensive (especially in large graphs). Instead, we can use Dijkstra's algorithm, which works as follows:

1. Create a priority queue of nodes to visit, initialized with the start node and its distance (which is 0).
2. While there are nodes in the queue:
   * Pop the node with the smallest distance from the queue.
   * If we have already visited that node, skip it.
   * Otherwise, mark the node as visited and update the distances to its neighboring nodes if they can be improved.
3. Once we have visited all reachable nodes, return the `distances` array.

By using a priority queue to visit nodes in order of increasing distance, Dijkstra's algorithm ensures that we always consider the shortest path to each node first. This is what enables us to find the shortest paths to all nodes efficiently.

By computing the shortest distances to each node using dynamic programming and Dijkstra's algorithm, we can solve the single-source shortest path problem in O(m log n) time, where `m` is the number of edges and `n` is the number of nodes in the graph. This is much faster than the brute force approach of considering all possible paths, which would take O(n^m) time.

## Usage

To use the `dijkstra` function, simply provide a dictionary `graph` representing the weighted graph and a starting node `start`. The `graph` parameter should be a dictionary of dictionaries, where the outer dictionary maps nodes to their neighboring nodes and the inner dictionaries map neighboring nodes to their edge weights. For example, a graph with nodes `A`, `B`, and `C` and edges `(A, B)` with weight 1 and `(A, C)` with weight 2 would be represented as follows:

```python
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {},
    'C': {}
}
```

The `start` parameter represents the node to start the search from. The function returns a dictionary containing the shortest distances to each node from the start node.

```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}
start = 'A'

distances = dijkstra(graph, start)
print("Shortest distances from", start)
for node, distance in distances.items():
    print(node, ":", distance)
```

This will output the following result:

```
Shortest distances from A
A : 0
B : 1
C : 3
D : 4
```

which means that the shortest distance from node `A` to nodes `B`, `C`, and `D` (given the weighted graph defined by the `graph` dictionary) are 1, 3, and 4, respectively.