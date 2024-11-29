# write a function that takes the radius of a circle and returns the area of the circle
# use the formula: area = pi * r^2
# where pi = 3.14159
# test the function with a radius of 5 and 10
# print the result to the console

import math

def area_of_circle(radius):
    return math.pi * radius**2

print(area_of_circle(5))
print(area_of_circle(10))
