'''Write a program to display the count of even and odd numbers in a given range.
Sample Input
Start: 20
End : 50
(inclusive of 20 and 50)
Sample Output:
Even : 16
Odd : 15'''

s=int(input("Enter starting range: "))
e=int(input("Enter end range: "))
i=s
ecount=0
ocount=0
while i<=e:
    if i%2==0:
        ecount+=1
    else:
        ocount+=1
    i+=1
print("Even count is : ",ecount)
print("Odd count is : ",ocount)