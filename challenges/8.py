import math

radius = float(input("What is the radius of the circle? "))
rounder = int(input("To what decimal place should the area be? "))
area = math.pi * (radius ** 2)
area2 = round(area, rounder)
print(f"The area is {area2}")
