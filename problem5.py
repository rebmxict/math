# Problem: We would love to draw a circle with center {x:xC,y:yC,z:zC} and radius R within a plane having a normal vector (xN,yN,zN). How to compute 24 points equaly spaced belonging to this circle?

# center: Coordinates of the center point of the circle
# normal_vector: Normal vector of the plane

import math

def compute_circle_points(center, radius, normal_vector, num_points=24):
    points = []

    for i in range(num_points):
        angle = 2 * math.pi * i / num_points
        cos_angle = math.cos(angle)

        # Parametric equations for a circle in 3D space
        x = center['x'] + radius * (cos_angle * normal_vector['x'])
        y = center['y'] + radius * (cos_angle * normal_vector['y'])
        z = center['z'] + radius * (cos_angle * normal_vector['z'])

        points.append((x, y, z))

    return points

center = {'x': 1, 'y': 2, 'z': 3}
radius = 5
normal_vector = {'x': 1, 'y': 0, 'z': 0}

circle_points = compute_circle_points(center, radius, normal_vector)
print(circle_points)