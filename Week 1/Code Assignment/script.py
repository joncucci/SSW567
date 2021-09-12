
'''

Author: Jon Cucci
SSW-567 HW#1 Testing Classify Triangle
9/10/21

'''

import math
import pytest

# Triangle classification
def classify_triangle(a, b, c):

    result = []
    a, b, c = sorted([a,b,c])

    # Filter invalid cases
    if (a<=0 or b<=0 or c<=0) or not ((a + b > c) and (a + c > b) and (b + c > a)):
        result.append("Invalid Triangle")

    # Equilateral Triangle Classification
    elif (a == b == c):
        result.append("Equilateral Triangle")

    else:
        # Right Triangle classification
        if round(a**2, 6) + round(b**2, 6) == round(c**2, 6):
            result.append("Right Triangle")

        # Isosceles Triangle Classification
        if (a in [b, c]) or (b in [a, c]):
            result.append("Isosceles Triangle")

        # Scalene Triangle Classification
        if (a != b != c):
            result.append("Scalene Triangle")

        # An invalid triangle input.
        if result == []:
            result.append("Invalid Triangle")

    result = (" and ").join(result)
    print(result)
    return result

# Tests
def main():

    assert classify_triangle(5,4,3) == "Right Triangle and Scalene Triangle"
    assert classify_triangle(1, 1, math.sqrt(2)) == "Right Triangle and Isosceles Triangle"

    assert classify_triangle(1,1,1) == "Equilateral Triangle"
    assert classify_triangle(10000,10000,10000) == "Equilateral Triangle"

    assert classify_triangle(2, 3, 4) == "Scalene Triangle"
    assert classify_triangle(4, 6, 8) == "Scalene Triangle"

    assert classify_triangle(1, 1, 100000) == "Invalid Triangle"
    assert classify_triangle(-3, -4, -5) == "Invalid Triangle"
    assert classify_triangle(-4, 5.334324, 1000003232432) == "Invalid Triangle"

if __name__ == "__main__":
    main()