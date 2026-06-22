算法问题

- 从cheapestnode开始，没必要，因为run out 每个node才得出路径

The algorithm exists in many variants; Dijkstra's original variant found the shortest path between two nodes,[3] but a more common variant fixes a single node as the "source" node and finds shortest paths from the source to all other nodes in the graph, producing a shortest-path tree.



negative weight怎么就不行了



This algorithm will continue to run until all of the reachable vertices in a graph have been visited, which means that we could run Dijkstra’s algorithm, find the shortest path between any two reachable nodes, and then save the results somewhere. Once we run Dijkstra’s algorithm just once, we can look up our results from our algorithm again and again — without having to actually run the algorithm itself! The only time we’d ever need to re-run Dijkstra’s algorithm is if something about our graph data structure changed, in which case we’d end up re-running the algorithm to ensure that we still have the most up-to-date shortest paths for our particular data structure.



https://medium.com/basecs/finding-the-shortest-path-with-a-little-help-from-dijkstra-613149fbdc8e