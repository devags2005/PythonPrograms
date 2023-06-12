'''Write a program to display the multiplication table as below
Sample Input
5
Sample Output
5 * 1 = 5
5 * 2 = 10
.
.
5 * 10 = 50'''

print("Multiplication table")

n=int(input("Enter the number: "))

for i in range(1,11):
    print(i,"*",n,"=",i*n)