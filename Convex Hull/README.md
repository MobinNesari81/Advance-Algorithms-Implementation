# Convex Hull Problem

The Convex Hull of a set of points is the smallest convex polygon that contains all the points in the set. In other words, it's the boundary of the shape that encloses all the points in the set while remaining convex.

In the image above, the Convex Hull of the points is shown in red. Notice how it's the smallest convex polygon that contains all the points.

Finding the Convex Hull of a set of points is an important problem in computational geometry and has many practical applications.

There are several algorithms for solving the Convex Hull problem, including Graham's Scan, Jarvis's March, and Chan's Algorithm. In this implementation, we use the Divide and Conquer approach to solve the problem.

## Divide and Conquer Approach

The Divide and Conquer approach involves dividing a problem into smaller subproblems, solving each subproblem independently, and then combining the solutions to obtain the solution to the original problem. The algorithm works in three steps: divide, conquer, and combine.

1. **Divide**: We divide the set of points into two equal-sized subsets.
2. **Conquer**: We recursively find the Convex Hull for each subset using the same algorithm.
3. **Combine**: We merge the two Convex Hulls obtained from the two subsets to get the final Convex Hull.

The base case for the recursion is when the number of points in a subset is less than 4. For small sets of points, we can simply compute the Convex Hull using another algorithm, such as Graham's Scan.

To merge the two Convex Hulls obtained from the two subsets, we need to find the upper and lower tangent lines of the two Convex Hulls. We then merge the two chains obtained by removing the points that lie between the two tangent lines, and finally compute the Convex Hull of the merged chain.

## Implementation

The implementation provided above uses a `Point` class to represent each point in the set. The `convex_hull()` function takes a list of points as its argument and returns the Convex Hull of the set using Graham's Scan. The `merge_hulls()` function takes the two Convex Hulls obtained from the two subsets and merges them to obtain the final Convex Hull using the Divide and Conquer approach. Finally, the `convex_hull_dc()` function is the main function that recursively divides the set of points into smaller subsets, solves each subset independently, and merges the solutions to obtain the final Convex Hull using the Divide and Conquer approach.

To use this implementation, you can create a list of `Point` objects and then call the `convex_hull_dc()` function with that list as an argument. The function will return the list of `Point` objects that form the Convex Hull.

```python
points = [Point(0, 3), Point(2, 2), Point(1, 1), Point(2, 1),
          Point(3, 0), Point(0, 0), Point(3, 3)]

hull = convex_hull_dc(points)

for p in hull:
    print("({},{})".format(p.x, p.y))
```

This will output:

```
(0,0)
(3,0)
(3,3)
(0,3)
```

Note: This implementation assumes that there are no duplicate points in the set. If there are duplicates, they may be included in the Convex Hull and need to be removed manually.