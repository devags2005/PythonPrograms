'''A company has decided to give bonuses to their employees based on their service.
More than 10 Years: 10%
More than 6 years and less than 10–8%
Less than 6 years: 5%
Ask the user to enter the salary and year of service and print their bonus.'''

name=input("Enter your name: ")
sa=int(input("Enter your salary: "))
yr=int(input("Enter your years of service: "))
if yr>=10:
    bonus=sa*(10/100)
    t=sa+bonus
    print("Your bonus is: ",t)
elif yr>=6 or yr<=9:
    bonus=sa*(8/100)
    t=sa+bonus
    print("Your bonus is: ",t)
elif yr<=5:
    bonus=sa*(5/100)
    t=sa+bonus
    print("Your bonus is: ",t)

else :
    print("Sorry you don't have enough years of experience")
