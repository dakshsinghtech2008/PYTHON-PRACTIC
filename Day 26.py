#Write a Python program using nested while loops to print the following pattern:
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
#1 2 3 4 5
x=1
while x<=5 :
    j=1
    while j<=5 :
        print(j, end=' ')
        j=j+1
    print()
    x=x+1