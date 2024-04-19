def min_uncovered_length(a, b):
    # a: length of the northern side of the house
    # b: length of each brick
    
    # Find the maximum number of bricks that can be placed
    num_bricks = a // b
    
    # Calculate the covered length
    covered_length = num_bricks * b
    
    # The uncovered length is the remaining part
    uncovered_length = a - covered_length
    
    return uncovered_length

# Read input
a, b = map(int, input().split())

# Call the function and print the result
print(min_uncovered_length(a, b))