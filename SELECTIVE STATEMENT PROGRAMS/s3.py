'''Check if the nth power of a number is even or not (get the number and the power as
an input).'''

n=int(input("Enter num:"))
p=int(input("Enter pow:"))
a=n**p
print(a)
if(a%2==0):
    print("Even")
else:
    print("not even")