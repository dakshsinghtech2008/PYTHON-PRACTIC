#Write a Python program to input a 5-digit number and print its reverse. 
#If the entered number is not a 5-digit number, display an appropriate message.
x = int(input("ENTER 5 DIGIT NUMBER : "))
y=x
count = 0
while y>0:
    y=y//10
    count = count + 1
if count == 5:
    A=x
    B= 0
    while A>0:
        digit=A % 10
        B= B*10+digit
        A= A//10
    print("REVERSE :", B)
else:
    print("PLEASE ENTER ONLY 5 DIGIT NUMBER")