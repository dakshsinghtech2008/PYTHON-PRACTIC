#Write a Python program to count the total number of digits in a given number using a while loop.
x = int(input("ENTER A NUMBER : "))
count = 0
while x > 0:
    x = x // 10
    count = count + 1
print("TOTAL DIGITS :", count)