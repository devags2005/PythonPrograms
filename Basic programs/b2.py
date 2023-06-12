'''Write a Python program to calculate the surface volume and area of a cylinder.
Formula:
Volume = pi * radius * radius * height
Surface area of a cylinder = ((2*pi*radius)*height) + ((pi*radius**2)*2)'''

r=int(input("Enter radius:"))
h=int(input("Enter height:"))
def cylinder(r,h):
    volume=3.14*r*r*h
    surfacearea=(2*3.14*r*h)+(2*3.14*r*r)
    print("volume and area is:",volume,surfacearea)
cylinder(r,h)