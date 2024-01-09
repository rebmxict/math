# Problem: Given two straight lines, how to compute the intersection ?

# m1: Slope of the first line.
# c1: Y-intercept of the first line (the value of y when x = 0 for the first line).
# m2: Slope of the second line.
# c2: Y-intercept of the second line (the value of y when x = 0 for the second line).

def are_lines_intersecting(m1, c1, m2, c2):
    # Check if slopes are different (lines intersect at a single point)
    if m1 != m2:
        return True
    # Check if slopes are equal and y-intercepts are equal (infinite intersections)
    elif m1 == m2 and c1 == c2:
        return True
    # Otherwise, lines are parallel and do not intersect
    else:
        return False

m1, c1 = 2, 1  # slope and y-intercept of line 1
m2, c2 = -1, 3  # slope and y-intercept of line 2

result = are_lines_intersecting(m1, c1, m2, c2)
print(result)