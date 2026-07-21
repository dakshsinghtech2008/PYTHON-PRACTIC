# Write a Python program using the if-elif-else statement to display the first 10 multiples based on the user's choice:

# Press 1 → Display the table of 2
# Press 2 → Display the table of 3
# Press 3 → Display the table of 4
# Press 4 → Display the table of 5
# Otherwise, display "INVALID NUMBER".
x = int(input("PRESS ONE NUMBER : "))

if x == 1:
    print(2, 4, 6, 8, 10, 12, 14, 16, 18, 20)

elif x == 2:
    print(3, 6, 9, 12, 15, 18, 21, 24, 27, 30)

elif x == 3:
    print(4, 8, 12, 16, 20, 24, 28, 32, 36, 40)

elif x == 4:
    print(5, 10, 15, 20, 25, 30, 35, 40, 45, 50)

else:
    print("INVALID NUMBER")