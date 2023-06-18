'''Write a python program which reads your mail id, and extract the username from
the mail id and generate the password such as username and the reverse of it.'''

str1=input("Enter your mailid: ")
x=str1.split("@")[0]
print("your username is : ",x)
y=x[::-1].upper()
print("Password: ",x+y)