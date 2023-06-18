'''Write a Python code with the function interest_calculation() which calculates the
simple interest. The program should take the name of the customer, age of the
customer, gender (‘M’ or ‘F’), principal amount (P), and number of years (N) as
input.
If the customer is a senior citizen, fix the rate of interest (R) at 12%, if the customer
is “female,” fix the rate of interest (R) at 10%; and for others, fix the rate of interest
(R) at 9%.
The function should take P, N, and R values as parameters.'''

name=input("Enter your name: ")
age=int(input("Enter your age: "))
gen=input("Enter gender(M/F): ")
p=int(input("Enter Principal amount: "))
n=int(input("Enter number of years: "))

def SI(p,n,r):
    si=(p*r*n)/100
    print("SI is",si)
    
if age>=60:
    r=12
    SI(p,n,r)
elif age<60 and gen=='F':
    r=10
    SI(p,n,r)
elif age<60 and gen=='M':
    r=9
    SI(p,n,r)
else:
    print("Invalid entry")
    