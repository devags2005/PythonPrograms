''' A Rotary Club has decided to conduct a blood donation camp. The eligibility criteria
for the blood donation camp will be that the person should be above 18 and his or
her weight should be above 40. The volunteers will enter the name, age, and weight
of the person, and then it will display whether they are eligible or not.
Display "1" if they are eligible and "0" if they are not eligible'''

name=input("Enter your name: ")
bg=input("Enter your blood group: ")
age=int(input("Enter your age: "))
wg=int(input("Enter your weight in kgs: "))
result=print("1") if age>18 and wg>40 else print("0")

