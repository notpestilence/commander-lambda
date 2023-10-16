# 4.2. Running with Bunnies

You and your rescued bunny prisoners need to get out of this collapsing death trap of a space station - and fast! Unfortunately, some of the bunnies have been weakened by their long imprisonment and can't run very fast. Their friends are trying to help them, but this escape would go a lot faster if you also pitched in. The defensive bulkhead doors have begun to close, and if you don't make it through in time, you'll be trapped! You need to grab as many bunnies as you can and get through the bulkheads before they close.

The time it takes to move from your starting point to all of the bunnies and to the bulkhead will be given to you in a square matrix of integers. Each row will tell you the time it takes to get to the `start`, `first bunny`, `second bunny`, ..., `last bunny`, and the `bulkhead` in that order. The order of the rows follows the same pattern $(start, bunnies, bulkhead)$. The bunnies can jump into your arms, so picking them up is instantaneous, and arriving at the bulkhead at the same time as it seals still allows for a successful, if dramatic, escape. (Don't worry, any bunnies you don't pick up will be able to escape with you since they no longer have to carry the ones you did pick up.) You can revisit different spots if you wish, and moving to the bulkhead doesn't mean you have to immediately leave - you can move to and from the bulkhead to pick up additional bunnies if time permits.

In addition to spending time traveling between bunnies, some paths interact with the space station's security checkpoints and add time back to the clock. Adding time to the clock will delay the closing of the bulkhead doors, and if the time goes back up to $0$ or a positive number after the doors have already closed, it triggers the bulkhead to reopen. Therefore, it might be possible to walk in a circle and keep gaining time: that is, each time a path is traversed, the same amount of time is used or added.

Write a function of the form `solution(times, time_limit)`to calculate the most bunnies you can pick up and which bunnies they are, while still escaping through the bulkhead before the doors close for good. If there are multiple sets of bunnies of the same size, return the set of bunnies with the lowest prisoner IDs (as indexes) in sorted order. The bunnies are represented as a sorted list by prisoner ID, with the first bunny being $0$. There are at most $5$ bunnies, and `time_limit` is a non-negative integer that is at most $999$.

For example, with a time limit of $1$, we have:
```py
[
 [0, 2, 2, 2, -1],  # 0 = Start
 [9, 0, 2, 2, -1],  # 1 = Bunny 0
 [9, 3, 0, 2, -1],  # 2 = Bunny 1
 [9, 3, 2, 0, -1],  # 3 = Bunny 2
 [9, 3, 2, 2,  0],  # 4 = Bulkhead
]
```
The five inner array rows designate the starting point, bunny 0, bunny 1, bunny 2, and the bulkhead door exit respectively. You could take the path 0 -> 4 -> 2 -> 4 -> 3 -> 4, that is:
```
Start  End  DeltaTime Status
 -      0       -     1        Bulkhead initially open
 0      4      -1     2
 4      2       2     0
 2      4      -1     1
 4      3       2    -1        Bulkhead closes
 3      4      -1     0        Bulkhead reopens; you and the bunnies exit
```
With this solution, you would pick up bunnies 1 and 2. This is the best combination for this space station hallway, so the answer is `[1, 2]`.

---

# Explanation
As with other previous graph problems, we are presented with an adjacency  matrix. Firstly, there are a few edge cases to consider:
* If there are exactly 2 rooms (i.e., the adjacency matrix is exactly of size $2\times2$), the procedure only involves transitioning to the subsequent room, identified as the bulkhead.  
* If there is only one room, we can just exit since the starting room is already the bulkhead.

After addressing both edge cases, we first check whether the graph contains a negative cycle. The rationale is that it allows us to run around the cycle enough times before saving the bunnies. Conveniently, this can be achieved with [Bellman-Ford algorithm](https://doi.org/10.1137/1.9781611973020.6), where the core idea pertains to relaxation -- edges are constantly replaced by better and better ones until they eventually reach the solution.

Implementation of the algorithm is as follows:
1. Initialise a distance matrix $d$ with maximum values (`sys.maxsize`) for all distances
2. Set the diagonal elements to 0, and iteratively "relax" the distances while checking for negative cycles.
3. If a negative cycle is found that can be reached from starting node without exceeding the time limit, it returns `True` and $d$. Otherwise, it returns `False`.

If a negative cycle indeed exists, one can keep traveling in that cycle repeatedly, so the function returns all bunnies except for the start and end points (see line 37-38 on `solution.py`). Otherwise:

1. Perform BFS with respect to the current position, the path taken so far, the time left, and the visited nodes -- all aggregated under one stack. Each iteration keeps track of the bunnies rescued.
2. BFS searches for all available paths, adding nodes to the path if there's enough time to reach them. In other words, we consider a path is feasible as long as we have enough time.
3. When a path reaches the last node, it checks if it has collected all bunnies. If so, we return the path as the maximum set of bunnies. 
4. If we've arrived at the last node without all the bunnies, we return a sorted list of bunnies (indices) to rescue.