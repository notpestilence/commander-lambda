# 4.1. Escape Pods

You've blown up the LAMBCHOP doomsday device and relieved the bunnies of their work duries -- and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time.

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function `solution(entrances, exits, path)` that takes 3 arguments:

* An array of integers denoting where the groups of gathered bunnies are;
* An array of integers denoting where the escape pods are located;
* An array of an array of integers of the corridors.

The function should return the total number of bunnies that can get through at each time step as an `int`. 

The entrances and exits are disjoint and thus will never overlap. The path element $path[A][B] = C$ describes that the corridor going from $A$ to $B$ can fit $C$ bunnies at each time step. There are at most 50 rooms connected by the corridors, and at most 2,000,000 bunnies that will fit at a time.

For example, if we have:
```py
entrances = [0, 1]
exits = [4, 5]
path = [
[0, 0, 4, 6, 0, 0], # Room 0: Bunnies
[0, 0, 5, 2, 0, 0], # Room 1: Bunnies
[0, 0, 0, 0, 4, 4], # Room 2: Intermediate room
[0, 0, 0, 0, 6, 6], # Room 3: Intermediate room
[0, 0, 0, 0, 0, 0], # Room 4: Escape pods
[0, 0, 0, 0, 0, 0], # Room 5: Escape pods
]
```

Then in each time step, the following might happen:
* 0 sends 4/4 bunnies to 2, and 6/6 bunnies to 3
* 1 sends 4/5 bunnies to 2, and 2/2 bunnies to 3
* 2 sends 4/4 bunnies to 4, and 4/4 bunnies to 5 <-- 8 bunnies escaped
* 3 sends 4/6 bunnies to 4, and 4/6 bunnies to 5 <-- 8 bunnies escaped

So, in total, 16 bunnies could make it to the escape pods (rooms 4 and 5) at each time step. In the above example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6 (or vice versa), but the final solution remains the same.

---

# Explanation
This is quite the challenge for me, despite prior experience with graph theory. Essentially this is a max flow problem, where we start with source nodes $s$ (rooms 0 and 1), traversing through nodes until we reach the sink nodes $t$ (rooms 4 and 5) while adhering to the capacity constraints for each edge. 

One option is a 'greedy' approach, that is, to always select edges with the most capacities. However, such an approach may lead to suboptimal results (i.e., [blocking flow](https://courses.csail.mit.edu/6.854/16/Notes/n10-blocking_flows.html)). Immediately this brings us to one of the most popular implementations for this problem: the [Ford-Fulkerson algorithm](https://doi.org/10.4153%2FCJM-1956-045-5). One additional lecture that I've found very helpful is [GE330 (Operations Research)](http://www.ifp.illinois.edu/~angelia/ge330fall09_maxflowl20.pdf) from the University of Illinois.

Basically, the algorithm first initialises all zeros (or infinites) for all edges. Then, at each iteration of the algorithm:
1. Traverse graph to see whether there's a path from $s$ to $t$. Such paths are commonly referred to as "augmenting paths".
2. If no augmenting path is found, the algorithm terminates, therefore the maximum flow is 0.
3. Otherwise, determine the maximum amount of flow that can be sent along that path. 
4. Compute each edges' residuals by subtracting the capacity $C(e)$ by the incoming flow $f(e)$ (i.e., how many capacities remain after being fed $f(e)$ ) -- for instance, if $C(u,v)$ is $5$ and $f(u,v)$ is $3$, the residual $C(v,u)$ will be $2$.
5. Make a copy of the original graph (called residual graph) where for forward edges (edges in the original graph; $C(u,v)$ ), decrease the residual capacity by the flow added, and for reverse edges (edges added to represent the reverse flow, $C(v,u)$ ), increase the residual capacity by the same amount. 
6. Recompute potential augmenting paths, updating the residual graph necessarily.
7. When no more augmenting paths can be found, the algorithm terminates, and the flow achieved at this point is the maximum flow in the network.

My implementation uses BFS to search augmenting paths, effectively rendering this into [Edmonds-Karp Algorithm](https://dl.acm.org/doi/10.1145/321694.321699). This 'upgrade' effectively speeds up the search process -- accounting for the shortest path with available capacities. 

One final consideration is that our problem incorporates multiple-source multiple-sink setup. That is, instead of $s$ and $t$ being in one node each, our problem presents multiple. This can be easily thwarted by introducing a dummy node for both $s$ and $t$ (e.g., an additional dummy source/sink node that is connected to the original nodes with infinite capacity links) -- see the function `add_dummy_node(entrances, exits, path)` for implementation details.

Inside this directory is also a useful lecture note from Stanford, under the filename `CS261 A Second Course in Algorithms Lecture 1 Course Goals and Introduction to Maximum Flow.pdf`
