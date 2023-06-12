'''Three numbers form a Pythogorean triple if the sum of the squares of two numbers
is equal to the square of the third.
For example, 3, 4, and 5 form a Pythagorean triple since 3*3 + 4*4 = 5*5.
Enter the three numbers n1, n2, and n3 (they should be in increasing order). If
they form a Pythoagorean triple, then print ‘1," otherwise print ‘0’.'''

a,b,c=map(int,input("Enter triangle sides with space :").split())
sum=(a**2)+(b**2)
result=print("1") if sum==(c**2) else print("0")