# Sum of brackets

for this quesrion i ran into optimization poblem but i somhow solved it
rn i can't find the better solution so i post the normal one.


The problem description is as follows:

You are given an integer n and a decimal number x.

You need to write a program to calculate the result of the following expression:

`[x] + [x + 1/n] + [x + 2/n] + ... + [x + (n-1)/n]`

Here,` [x] `represents the floor function, which is the largest integer less than or equal to x.


**The input format is as follows:**

`The first line contains the number of test cases t.`

**For each test case:**

`1)The first line contains a positive integer n.`

`2)The second line contains a decimal number x.`

**Constraints:** 1 ≤ t ≤ 100, 1 ≤ n ≤ 10^9, -100 < x < 100, x is given with at most 7 decimal places.
The output format is a single line containing the integer result of the expression.
