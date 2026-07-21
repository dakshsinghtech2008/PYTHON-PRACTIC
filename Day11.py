
# Write a Python program to create a Simple Calculator using if-else statements. The program should:

# Take an operator (+, -, *, /) from the user.
# Take two numbers as input.
# Perform the selected arithmetic operation.
# Display the result.
# If the user enters an invalid operator, display "INVALID ENTRY".
x=input("ENTER OPERATER (+, -, *, /): ")
y=int(input("ENTER THE FRIST NUMBER : "))
z=int(input("ENTER THE SECOND NUMBER : "))
if x=='+':
    print("ADD : ",y+z)
else :
    if x=='-' :
        print("SUBTRACT : ",y-z)
    else :
        if x=='*' :
            print("MULTIPLY : ",y*z)
        else :
            if x=='/' :
                print("DIVIDE : ",y/z)
            else :
                print("INVALID ENTRY")