'''Write a program to display the factors of a given number.
Sample Input
56
Sample output
1, 2, 4, 7, 8, 14, 28, 56'''

print("Factors of a number")

n=int(input("Enter the number: "))

for i in range(1,n+1):
    if n%i==0:
        print(i)
