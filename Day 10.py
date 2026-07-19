# Write a Python program that performs the following operations based on the user's choice:

# If the user enters 1, calculate and display the Area of a Circle.
# If the user enters 2, calculate and display the Perimeter of a Circle.
# If the user enters 3, calculate and display the Area of a Triangle.
# If the user enters any other number, display "Invalid Choice".
x=int(input(" ENTER THE NUMBER : "))
if x == 1:
    r=int(input("Enter radius: "))
    print("Area =", 3.14 * r * r)
else:
    if x==2:
        r =int(input(" ENTER THE RADIUS OF CRICLE : "))
        print("Perimeter =",2*3.14*r)
    else:
        if x==3:
            b=int(input(" ENTER THE BASE OF TRIANGLE : "))
            h=int(input(" ENTER THE HEIGHT OF TRIANGLE : "))
            print("Area =",(b*h)/2)
        else:
            print("Invalid Choice  ")
            