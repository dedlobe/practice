# Min uncovered length

The goal is to write a program in Python that takes the input values a and b and outputs the minimum uncovered length of the northern side of Moriarty's house.

# Explanation
The **min_uncovered_length** function takes two arguments: a (the length of the northern side of the house) and b (the length of each brick).

It calculates the **maximum number** of bricks that can be placed along the northern side by dividing a by b using integer division (//).
>This gives the number of complete bricks that can fit.

The covered length is then calculated by multiplying the number of bricks by the length of each brick (num_bricks * b).
The uncovered length is the remaining part of the northern side, which is calculated by subtracting the covered length from the total length **(a - covered_length)**.
>The function returns the uncovered length.

The program reads the input values of a and b from the user using the **input().split()** function, which splits the input string into **two values separated by a space**.

The **map(int, ...)** function is used to convert both input values to integers.

The **min_uncovered_length** function is called with the input values, and its result is printed to the console.
