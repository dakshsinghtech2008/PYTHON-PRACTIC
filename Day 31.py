#Write a Python program using nested while loops to print numbers from 1 to 25 in 5 rows and 5 columns, as shown below:
# 1  2  3  4  5
# 6  7  8  9  10
# 11 12 13 14 15
# 16 17 18 19 20
# 21 22 23 24 25
x = 1
y=1
while x <= 5:
    j = 1
    while j<=5:
        print(y, end=" ")
        y=y+1
        j=j+1
    print()
    x = x + 1
