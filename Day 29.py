#Write a Python program to create a dice game. Ask the user to enter two dice numbers for a maximum of 5 attempts. 
# If the sum of the two dice numbers is 6, display "YOU WIN THIS GAME"; otherwise, display "YOU LOSE THIS GAME. 
# PLEASE TRY AGAIN". If an invalid dice number (greater than 6) is entered, ask the user to enter a valid dice number.
x=1
while x<=5:
    A=int(input("ENTER FRIST DICE NUMBER : "))
    B=int(input("ENTER SECOND DICE NUMBER : "))
    if A<=6 and B<=6 :
        C=A+B
        if C==6 :
            print("YOU WIN THIS GAME .....")
            break
        else :
            print("YOU LOSE THIS GAME .PLESE TRY AGAIN ..... ")
        x=x+1
    else :
        print("ENTER VALID DICE NUMBER .....")
