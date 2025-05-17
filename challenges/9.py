base = float(input("What is the length of the base? "))
height = float(input("What is the length of the height? "))
rounder = int(input("To what decimal place should the area be? "))

area = (height * base) / 2
area2 = round(area, rounder)
print(f"The area of the triangle is {area2}")
