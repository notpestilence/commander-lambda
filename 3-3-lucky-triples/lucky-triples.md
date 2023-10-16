# 3.3. Lucky Triples

Given a list (from 1 to 2000 elements) of random integers (from 1 to 999999) write a function, `solution(l)` that accepts a list as input and returns the number of "lucky triples" present in the list.

For this purpose, a lucky triple is defined as a list of three numbers $(x,y,z)$ such that $x$ divides $y$, $y$ divides $z$, and $x≤y≤z$. So, for instance, $(2,4,8)$ is a lucky triple and so is $(1,1,1)$. 

As examples, calling `solution([1,1,1])` will return `1`, since there exist only one set of "lucky triples." On the other hand, calling `solution([1, 2, 3, 4, 5, 6])` will return 3, since there are three lucky triples:
* [1, 2, 4];
* [1, 2, 6];
* [1, 3, 6].

---

# Explanation

This is fairly solvable with simple dynamic programming. Firstly, we need to calculate "lucky doubles" with respect to each element in `l`. Specifically, for each element in `l`, we need to memoize previous number(s) which can evenly divide this current number. This is done by:
1. Initialising `c`, a list of zeros with the length of `l`. This will contain all "lucky doubles."
2. Iterating over the elements of `l` by index `i` (i.e., `l[i]`).
3. For each `l[i]`, iterate from `0` to `i - 1` (in here we call it `j`) to look at all the previous elements in the list.
4. If `l[i]` is divisible by `l[j]`: increment `c[i]` by 1 to indicate that one more number (`l[i]`) is divisible by `l[j]`. In this manner, `c[j]` now keeps track of how many previous numbers in the list divide `l[j]`.
5. `c[j]` is now the number of lucky triples that can be formed with the current element of the list (`l[i]`).
6. Repeat for each list element. 