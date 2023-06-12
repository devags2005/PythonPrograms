'''ACB, the Omni Bus Company, has decided to give a 20% traveling fare concession for
senior citizens; the actual fare will be Rs 1020. The upper age limit for senior
citizens is above 60.
For verification, they will ask for the date of birth (take the year alone), and if
satisfied, they will be given a concession and will be displayed the final traveling
charge; if not, the original fare will be displayed.'''

age=int(input("Enter your age:"))
year=int(input("Enter your year of birth:"))

if(2023-year)>=60 and age>=60:
    t=1020*(20/100)
    print("Your omni bus charge is:",t)
else:
    print("Your omni bus charge is 1020")