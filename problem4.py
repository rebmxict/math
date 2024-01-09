# Problem: How to get the projection of this point M on this plane?

# point_A: Coordinates of a point on the plane
# normal_vector: Normal vector of the plane
# point_M: Coordinates of the point to be checked


def project_point_onto_plane(point_M, point_A, normal_vector):
    dot_product = sum(n * (M - A) for n, M, A in zip(normal_vector, point_M, point_A))
    magnitude_squared = sum(n**2 for n in normal_vector)

    projection = [M - (dot_product / magnitude_squared) * n for M, n in zip(point_M, normal_vector)]
    return projection

# Example usage
point_M = [1, 2, 3]
point_A = [1, 2, 3]
normal_vector = [2, -1, 3]

projection = project_point_onto_plane(point_M, point_A, normal_vector)
print(projection)
