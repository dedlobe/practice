def minimum_blankets(n, d, animal_positions):
    # Sort the animal positions in ascending order
    animal_positions.sort()

    # Initialize the number of blankets needed
    blankets_needed = 0

    # Initialize the current position to the first animal's position
    current_position = animal_positions[0]

    # Iterate over the remaining animals
    for i in range(1, n):
        # If the next animal's position is too far from the current position
        if animal_positions[i] - current_position > d:
            # Place a new blanket and update the current position
            blankets_needed += 1
            current_position = animal_positions[i]

    #Add one more blanket for the last animal
    blankets_needed += 1

    return blankets_needed

# example usage
n, d = map(int, input().split())
animal_positions = list(map(int, input().split()))

result = minimum_blankets(n, d, animal_positions)
print(result)
