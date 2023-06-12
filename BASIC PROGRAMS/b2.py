'''Write a Python program to calculate the surface volume and area of a cylinder.
Formula:
Volume = pi * radius * radius * height
Surface area of a cylinder = ((2*pi*radius)*height) + ((pi*radius**2)*2)'''

def vol (r,h):
    vol=3.14*r*r*h
    return vol
def surface(r,h):
    surface=((2*3.14*r)*h)+((3.14*r**2)*2)
    return surface
r= float(input("Enter the Radius:"))
h= float(input("Enter the height:"))
volume=vol(r,h)
area=surface(r,h)
print("The volume is",volume)
print("The surface area is",area)