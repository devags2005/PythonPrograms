'''Write a python program that reads integers from the user and stores them in a list.
Your program should continue reading values until the user enters 0. Then it
should display all of the values entered by the user (except for the 0) in ascending
order, with one value appearing on each line. Use either the sort method or the
sorted function to sort the list.'''


l1=[]
for i in range(1,500):
    n=int(input("Enter elements: "))
    if n==0:
        break
    else:
        l1.append(n)
l1.sort()
print(l1)