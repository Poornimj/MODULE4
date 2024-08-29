import random

numPoints = int(input("Enter the number of random points to generate:"))

insideCircle = 0

for _ in range(numPoints):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 < 1:
        insideCircle +=1

print(f"Inside circle value {insideCircle}")
piEstimate = 4*insideCircle / numPoints

print(f"Approximation of pi using {numPoints} random points: {piEstimate}")
