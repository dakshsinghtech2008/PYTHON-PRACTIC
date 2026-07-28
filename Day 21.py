#Write a Python program to input a number and check whether it is divisible by 3, 
#divisible by 5, divisible by both 3 and 5, or not divisible by either of them.
x=int(input("ENTER ONE NUMBER : "))
if x%5==0 and x%3==0 :
    if x%3==0 :
        print("DIVIDED BY 3 ")
    elif x%5==0 :
        print("DIVIDED BY 5 ")
else : 
     print("NUMBER NOT DIVIDED BY 5 & 3")