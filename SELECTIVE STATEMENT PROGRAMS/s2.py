'''Accept three sides of the triangle and check whether the triangle is possible or not.'''

a,b,c=map(int,input("Enter the sides with space").split())
if (a+b)>=c and (a+c)>=b and (b+c)>=a:
    print("triangle possible")
else:
    print("not possible")