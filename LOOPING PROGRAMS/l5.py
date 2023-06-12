'''Write a program to display the multiplication table as below with a given range
Sample Input
Start Table : 5
End Table: 8
Sample Output
5 * 1 = 5 6 * 1 = 6 7 *1 = 7 8*1 = 8
5 * 2 = 10 6*2 = 12 7*2=14 8*2= 16
.
.
5 * 10 = 50'''

print("Tables")

n=int(input("Enter start number: "))
e=int(input("Enter end number: "))

i=n
while i<=e:
    for j in range(1,11):
        print(j,"*",i,"=",j*i)
    i+=1