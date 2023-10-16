# 2.1. Bunny Worker Locations

The LAMBCHOP doomsday device takes up much of the interior of Commander Lambda's space station, and as a result the prison blocks have an unusual layout. They are stacked in a triangular shape, and the bunny prisoners are given numerical IDs starting from the corner, as follows:
```
| 7
| 4 8
| 2 5 9
| 1 3 6 10
```
Each cell can be represented as points (x, y), with x being the distance from the vertical wall, and y being the height from the ground.

For example, the bunny prisoner at (1, 1) has ID 1, the bunny prisoner at (3, 2) has ID 9, and the bunny prisoner at (2,3) has ID 8. This pattern of numbering continues indefinitely. Write a function `answer(x, y)` which returns the prisoner ID of the bunny at location (x, y)

---

# Explanation

This was fairly hard initially, due to me not recognising the pattern in the example as [triangular numbers](https://byjus.com/maths/triangular-numbers/). If one ever studied arithmetic progression, one may realise the x and y axis represent a similar sequence. In my approach, we first find the x-axis location by a general triangular number formula (hint: [Find Tn](https://en.wikipedia.org/wiki/Triangular_number)), before finding the y-axis location by arithmetic sequence.