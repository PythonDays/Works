#import necessary libraries
import math

#define function to calculate the area of a circle
def area_of_circle(radius):
    return math.pi * radius**2

#define function to calculate the circumference of a circle
def circumference_of_circle(radius):
    return 2 * math.pi * radius

#define function to calculate the volume of a sphere
def volume_of_sphere(radius):
    return (4/3) * math.pi * radius**3

#define function to calculate the surface area of a sphere
def surface_area_of_sphere(radius):
    return 4 * math.pi * radius**2