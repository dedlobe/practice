def find_winner(loop, length, cars):
    # Calculate the time taken by each car to complete the race
    race_times = []
    for t, v in cars:
        time = (loop * length) / v + t
        race_times.append(time)

    # Find the car with the minimum race time
    winner = race_times.index(min(race_times)) + 1
    return winner

# Example input
loop, length = map(int, input().split())
n = int(input())
cars = [tuple(map(int, input().split())) for _ in range(n)]

# Find the winner and print the result
print(find_winner(loop, length, cars))
