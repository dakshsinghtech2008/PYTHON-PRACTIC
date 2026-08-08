#Write a Python program using nested while loops to print the following pattern:
# 1 1 1 1 1
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
x=1
a=1
while x<=5 :
    y=1
    while y<=5 :
        print(a, end=' ')
        y=y+1
    a=a+1
    print()
    x=x+1