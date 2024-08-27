import random

def estimate_pi(num_points):
    inside_circle = 0

    for _ in range(num_points):

        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x ** 2 + y ** 2 < 1:
            inside_circle += 1

    pi_estimate = 4 * inside_circle / num_points
    return pi_estimate

num_points = int(input("Enter the number of random points to generate: "))

approximation_of_pi = estimate_pi(num_points)

print(f"Approximation of pi using {num_points} random points: {approximation_of_pi}")