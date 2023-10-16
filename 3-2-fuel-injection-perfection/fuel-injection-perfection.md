# 3.2. Fuel Injection Perfection

Commander Lambda has asked for your help to refine the automatic quantum antimatter fuel injection system for her LAMBCHOP doomsday device. It's a great chance for you to get a closer look at the LAMBCHOP - and maybe sneak in a bit of sabotage while you're at it - so you took the job gladly.

Quantum antimatter fuel comes in small pellets, which is convenient since the many moving parts of the LAMBCHOP each need to be fed fuel one pellet at a time. However, minions dump pellets in bulk into the fuel intake. You need to figure out the most efficient way to sort and shift the pellets down to a single pellet at a time.

The fuel control mechanisms have three operations:

* Add one fuel pellet 
* Remove one fuel pellet
* Divide the entire group of fuel pellets by 2 (due to the destructive energy released when a quantum antimatter pellet is cut in half, the safety controls will only allow this to happen if there is an even number of pellets) 

Write a function called `solution(n)` which takes a positive integer as a string and returns the minimum number of operations needed to transform the number of pellets to 1. The fuel intake control panel can only display a number up to 309 digits long, so there won't ever be more pellets than you can express in that many digits.

For example: `solution(4)` returns 2: 
```
4 -> 2 -> 1
```
As another example, `solution(15)` returns 5: 
```
15 -> 16 -> 8 -> 4 -> 2 -> 1
```


---

# Explanation

This problem is related to [Least Significant Bit](https://en.wikipedia.org/wiki/Bit_numbering) (LSB) of decimals, being the rightmost (i.e., lowest-order) bit in a binary number. 
For instance, given an integer 42, the binary integer would be 101010. In this case, the LSB is 0. 

Hence, given an arbitrary binary number, the LSB can only be either 1 or 0. Based on this knowledge, there are two distinct cases that can happen for any given integer:

1. The LSB is 0
2. The LSB is 1

Notably, only even integers would have an LSB of 0, hence the third rule where division can only occur whenever there is an even number of pellets. 

## LSB is 0
If the LSB is 0, it does not make sense to add nor subtract since we can reach `1` faster if we divide it by 2. We could instead try 2 additions and then a division, but then that same result can be achieved in two steps: divide and add. Similarly with 2 subtractions. 

To demonstrate, let's say we'd want to reduce 30 to 1 using the least steps possible. Applying all three operations on the initial 30. yield us the following:

```
First op: 30 > 31 > 32 > 16 > 8 > 4 > 2 > 1  
Second op: 30 > 29 > 28 > 14 > 7 > 8 > 4 > 2 > 1
Third op: 30 > 15 > 16 > 8 > 4 > 2 > 1
```
We can see the third op only takes 6 operations, whereas the first and second ops took 7 and 8, respectively. Hence, if the LSB is 0, we can conduct division.

## LSB is 1
Here is where it gets tricky. If LSB is 1, there are four distinct possibilities:
* LSB ends with 001
* LSB ends with 011
* LSB ends with 111
* LSB ends with 101

We can break down each of them and try to come up with a solution for each case.
### LSB is 001
Given an arbitrary prefix bits `b`, if LSB is 001, applying the two applicable operations would be:
```
First op: b001 > b010 > b01 
Second op: b001 > b000 > b00
```
In two steps, the second operation yields 1 less than the former. We prove that the second op (subtraction) is better whenever LSB is 001. 

### LSB is 011
If LSB is 011, the two applicable operations would be:
```
First op: b011 > b100 > b10 > b1 > b
Second op: b011 > b010 > b01 > b00 > b0 > b
```
We understand the first operation (addition) reaches `b` faster. Therefore, if LSB is 011, addition is the way to go.

### LSB is 111
Similarly, we break down the two applicable operations if LSB is 111.
```
First op: b111 > b0000 > b000 > b00 > b0 > b
Second op: b111 > b110 > b11 > b000 > b00 > b0 > b
```
The first operation reaches `b` in 5 operations, wherein the second in 6. Therefore, if LSB is 111, addition is better than subtracting

### LSB is 101
Our last check pertains to when LSB is 101, as follows:
```
First op: b101 > b110 > b11 > b000 > b00 > b0 > b
Second op: b101 > b100 > b10 > b1 > b
```

It is clear that the second operation (subtraction) is more optimal with 4 steps, as opposed to the first with 6.

There are indeed a few exceptions. For instance, the integer 3 represents the binary `11`, which based on our proof above, should be performed addition. Instead, it should be subtracted and subtracted again:

```
First op: 3 > 4 > 2 > 1
Second op: 3 > 2 > 1
```

Python provides a built-in feature to convert any given input to its binary representation using the `bin()` function. From here it's just a series of ifs and elses.