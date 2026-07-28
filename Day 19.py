#Write a Python program using a while loop to
#input 10 numbers from the user and 
#print the sum of all even numbers.
i = 1
sum = 0
while i <= 10:
    x = int(input("ENTER ANY NUMBER : "))
    if x%2==0 :
        sum = sum + x
    i = i + 1
print("SUM OF ALL EVEN NUMBERS :", sum)
