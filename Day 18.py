#Write a Python program to input 10 numbers from the user and count how many are even and how many are odd. 
#Display the total count of even and odd numbers.

y=0
i=1
z=0

while i<=10 :
    x=int(input("enter any number : "))

    if x%2==0 :
        y=y+1
    else :
        z=z+1

    i=i+1
    
print("the even number are : ",y)
print("the odd number are : ",z)
       