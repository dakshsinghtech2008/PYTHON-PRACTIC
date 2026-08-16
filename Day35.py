#Write a Python program to input a 3-digit number and find the sum of all its digits using arithmetic 
# operators (`//` and `%`). Display the sum of the digits.**
x=int(input("ENTER ANY NUMBER : "))
z=x//10
A=x%10
B=z//10
C=z%10
S=A+B+C
print("SUM OF ALL DIGITS : ",S)