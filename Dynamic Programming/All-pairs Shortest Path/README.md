# All-Pairs Shortest Path with Dynamic Programming

This is a Python implementation of the all-pairs shortest path problem using dynamic programming and Floyd-Warshall algorithm. Given a weighted graph, the goal is to find the shortest paths between all pairs of nodes in the graph.

## Dynamic Programming Approach

The key idea behind the dynamic programming approach to this problem is to build up a table of the shortest paths between pairs of nodes in the graph. Specifically, we can define an array `distances` such that `distances[node1][node2]` represents the shortest distance from `node1` to `node2`. We can then fill in this array iteratively, starting with the direct distances between nodes (i.e., the edge weights) and working our way out to longer paths.

To find the shortest path between a pair of nodes `(node1, node2)`, we need to consider all possible paths from `node1` to `node2` and take the minimum of those distances. However, considering all possible paths would be prohibitively expensive (especially in large graphs). Instead, we can use Floyd-Warshall algorithm, which works as follows:

1. Initialize a copy of the input graph with missing edges assigned infinite weight.
2. For each intermediate node `intermediate_node`, compute the shortest path from each pair of nodes `start_node` and `end_node` through `intermediate_node`.
3. Return the `distances` array.

By computing the shortest paths between all pairs of nodes using dynamic programming and Floyd-Warshall algorithm, we can solve the all-pairs shortest path problem in O(n^3) time, where `n` is the number of nodes in the graph. This is much faster than the brute force approach of considering all possible paths, which would take O(n^(m+1)) time.

## Usage

To use the `floyd_warshall` function, simply provide a dictionary `graph` representing the weighted graph. The `graph` parameter should be a dictionary of dictionaries, where the outer dictionary maps nodes to their neighboring nodes and the inner dictionaries map neighboring nodes to their edge weights. For example, a graph with nodes `A`, `B`, and `C` and edges `(A, B)` with weight 1 and `(A, C)` with weight 2 would be represented as follows:

```python
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {},
    'C': {}
}
```

The function returns a modified version of the input `graph` dictionary containing the shortest paths between all pairs of nodes.

```python
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

shortest_paths = floyd_warshall(graph)
print("Shortest paths between all pairs of nodes:")
for node1 in shortest_paths:
    for node2 in shortest_paths[node1]:
        print(node1, "-", node2, ":", shortest_paths[node1][node2])
```

This will output the following result:

```
Shortest paths between all pairs of nodes:
A - A : 0
A - B : 1
A - C : 3
A - D : 4
B - A : inf
B - B : 0
B - C : 2
B - D : 5
C - A : inf
C - B : inf
C - C : 0
C - D : 1
D - A : inf
D - B : inf
D - C : inf
D - D : 0
```

which means that the shortest paths between all pairs of nodes (given the weighted graph defined by the `graph` dictionary) are:
- Node `A` to node `A`: 0
- Node `A` to node `B`: 1
- Node `A` to node `C`: 3
- Node `A` to node `D`: 4
- Node `B` to node `B`: 0
- Node `B` to node `C`: 2
- Node `B` to node `D`: 5
- Node `C` to node `C`: 0
- Node `C` to node `D`: 1
- Node `D` to node `D`: 0

