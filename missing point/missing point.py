def find_missing_corner(points):
    # Calculate the missing corner by XOR-ing the coordinates of all known corners
    missing_x = 0
    missing_y = 0
    missing_z = 0

    for x, y, z in points:
        missing_x ^= x
        missing_y ^= y
        missing_z ^= z

    return missing_x, missing_y, missing_z

# Read input
points = []
for _ in range(7):
    x, y, z = map(int, input().split())
    points.append((x, y, z))

# Find the missing corner
missing_corner = find_missing_corner(points)

# Print the result
print(*missing_corner)
