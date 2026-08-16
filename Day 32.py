#Write a Python program to input a 3-digit number and repeatedly divide it by 3 using a while loop for 3 times. 
# Display the result after each division. If the entered number is not a 3-digit number, display an appropriate message.
x = int(input("ENTER 3 DIGIT NUMBER : "))
z = 1
if x >= 100 and x <= 999:
    while z <= 3:
        y = x // 3    
        b=x % 3       
        print(y)
        z = z + 1
else:
    print("Enter Only 3 Digit Number")
