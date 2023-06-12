'''Write a program that displays a temperature conversion table for degrees Celsius
and degrees Fahrenheit. The table should include rows for all temperatures
between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns. The formula for converting
between degrees Celsius and degrees Fahrenheit
Sample Output
Celsius Fahrenheit
0 32.0
10 50.0
20 68.0
30 86.0
40 104.0
50 122.0
60 140.0
70 158.0
50 176.0
90 194.0
100 212.0'''

print("Celsius to Fahrenheit")

c=int(input("Enter end range: "))
print('C','F')
i=0
while(i<=c):
    f=((i*9)/5)+32
    print(i,f)
    i=i+10

