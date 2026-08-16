#Write a Python program using a while loop to print numbers from 1 to 10, 
# but skip printing the number 4 using the continue statement.
x=1
while x<=10:
    if x==4:
        x=x+1
        continue
    print(x)
    x=x+1