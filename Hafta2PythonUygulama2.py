import math
points = [(11, 120), (31, 42), (51, 60), (71, 28), (49, 10)]

"""
d = √(x₂-x₁)²+(y₂-y₁)²
"""

distances = []
distanceNotArray = None
def euclideanDistance (point1,point2):
    return math.sqrt(((point1[0]-point2[0]) ** 2 + (point1[1] - point2[1])**2))

for i in range(len(points)-1):
    distance = euclideanDistance(points[i], points[i + 1])
    distances.append(distance)

smallest_distance = min(distances)

print(f"En küçük Öklid mesafesi: {smallest_distance}")
