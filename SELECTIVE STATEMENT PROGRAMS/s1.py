'''Accept a number from the user and check whether it's a positive number or not.'''

n=int(input("Enter number:"))
if n>0:
    print("+ve num")
elif n<0:
    print("-ve num")
else:
    print("0")