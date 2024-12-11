

import math

# list of given points
points = [(1, 2), (4, 6), (7, 8), (2, 3)]

# function for calculating euclidean distance


def EucDistance(point1, point2):
    x1, y1 = point1  # unpacking the values from the tuples as x and y cordinates
    x2, y2 = point2
    distance = math.sqrt(math.pow(x2-x1, 2)+(math.pow(y2-y1, 2)))
    return distance


# empty list for all the distances
distances = []


for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = EucDistance(points[i], points[j])
        distances.append(distance)
        print(
            f"the distance between {points[i] }and {points[j]} is {distance}")
# find minimum distance from the list of distances
min_distance = min(distances)
print(f"the minimum distance is {min_distance}")
