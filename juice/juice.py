def maximize_happiness(n, V, juices):
    # Sort juices by happiness-to-volume ratio in descending order
    juices.sort(key=lambda x: x[0] / x[1], reverse=True)
    
    total_happiness = 0
    remaining_volume = V
    
    for h, v in juices:
        # Take the entire juice if there's enough volume
        if remaining_volume >= v:
            total_happiness += h
            remaining_volume -= v
        else:
            # Take a fraction of the juice
            total_happiness += (remaining_volume / v) * h
            break
    
    return total_happiness

# Get input from the user
n, V = map(int, input().split())

juices = []
for i in range(n):
    h, v = map(int, input().split())
    juices.append((h, v))

# Calculate maximum total happiness
result = maximize_happiness(n, V, juices)

# Print the result rounded to one decimal place
print(f"{result:.1f}")

