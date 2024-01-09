# Problem: Having a plane defined with a point A and a normal vector n. How to know if a point M is on this plane?

# point_A: Coordinates of a point on the plane
# normal_vector: Normal vector of the plane
# point_M: Coordinates of the point to be checked

def is_point_on_plane(point_M, point_A, normal_vector):
    # Check if the dot product is zero
    result = sum((n * (M - A)) for n, M, A in zip(normal_vector, point_M, point_A))

    return result == 0

# Example usage
point_M = [1, 2, 3]
point_A = [1, 2, 3]
normal_vector = [2, -1, 3]

result = is_point_on_plane(point_M, point_A, normal_vector)
print(result)