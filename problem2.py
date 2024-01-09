# Problem: Given a circle (center (xC,yC) and radius R) and a point M (xM,yM) create a function to get the projection P of M onto the circle.

# xC, yC: The coordinates of the center of the circle.
# R: The radius of the circle.
# xM, yM: The coordinates of the point to be projected onto the circle.

import math

def project_point_onto_circle(xC, yC, R, xM, yM):
    direction_vector = [(xM - xC), (yM - yC)]
    magnitude = math.sqrt(direction_vector[0]**2 + direction_vector[1]**2)
    normalized_vector = [(direction_vector[0] / magnitude), (direction_vector[1] / magnitude)]
    x_proj = xC + R * normalized_vector[0]
    y_proj = yC + R * normalized_vector[1]
    return x_proj, y_proj

xCircle, yCircle = 0, 0  # Center of the circle
radius = 5  # Radius of the circle
xPoint, yPoint = 13, 14  # Coordinates of the point

xProjection, yProjection = project_point_onto_circle(xCircle, yCircle, radius, xPoint, yPoint)

print(f"Original Point: ({xPoint}, {yPoint})")
print(f"Projected Point: ({xProjection}, {yProjection})")