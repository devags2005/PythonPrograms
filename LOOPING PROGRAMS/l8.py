'''Write a program to accept the numbers continuously; when we enter"-1” it should
stop accepting the input and at the same time display the number of even numbers
and odd numbers that were entered.'''

print("Accpeting input")

ecount=0
ocount=0
for i in range(1,100):
    i=int(input("Enter number: "))
    if i==-1:
        break
    if i%2==0:
        ecount+=1
    else:
        ocount+=1

print("Even count: ",ecount)
print("Odd count: ",ocount)