#Write a Python program using if-elif-else to display a menu and perform the selected operation.
#1. Area of Circle
#2. Perimeter of Circle
#3. Area of Square
#4. Area of Triangle
#The program should:
#Take the user's choice.
#Ask for the required input values.
#Display the result.
#If the user enters an invalid choice, display "INVALID NUMBER".
print("AREA OF CIRCLE = 1")
print("PERIMETER OF CIRCLE = 2")
print("AREA OF SQURE  = 3")
print("AREA OF TRIANGLE = 4")
x=int(input("PRESS ONE NUMBER : "))
if x==1 :
    r=int(input("ENTER THE RADIUS OF CRICLE : "))
    print("AREA OF CIRCLE : ",3.14*r*r)
elif x==2 :
    r=int(input("ENTER THE RADIUS OF CRICLE : "))
    print("PERIMETER OF CIRCLE : ",3.14*r*2)
elif x==3 :
    S=int(input("ENTER THE SIDE OF SQURE : "))
    print("AREA OF SQURE :",S*S)
elif x==4 :
    B=int(input("ENTER THE BASE OF TRIANGLE : "))
    H=int(input("ENTER THE HEIGHT OF TRIANGLE : "))
    print("AREA OF TRIANGLE : ",(B*H)/2)
else :
    print("INVALID NUMBER ")
