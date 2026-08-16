#Write a Python program to input a 3-digit number and check whether all three digits are equal. 
# If all digits are equal, print ACCEPTED; otherwise, print REJECT. 
# Also, display an appropriate message if the entered number is not a 3-digit number.
x = int(input("ENTER 3 DIGIT NUMBER : "))
if x >= 100 and x <= 999:
    a = x // 100
    b = (x // 10) % 10
    c = x % 10
    if a == b and b == c:
        print("ACCEPTED")
    else:
        print("REJECT")
else:
    print("Enter Only 3 Digit Number")