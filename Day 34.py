#Write a Python program to input a 3-digit number. Check whether the entered number contains exactly 3 digits using len() and str(). 
# If it is a 3-digit number, use a while loop to divide the number by 3 three times and print the result each time. 
# Otherwise, display an appropriate message.
x = int(input("ENTER 3 DIGIT NUMBER : "))
z = 1
if len(str(x))==3:
    while z <= 3:
        y = x // 3    
        b=x % 3       
        print(y)
        z = z + 1
else:
    print("Enter Only 3 Digit Number")
