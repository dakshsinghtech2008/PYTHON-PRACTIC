#ENTER 3 SUBJECT NUMBER AND PREDICT STUDENT PASS(>=50%) AND FAIL(<50%) AND TOTAL MARK IS  <=300 . 
X=int(input("ENTER THE MATH MARK : "))
Y=int(input("ENTER THE PHYSIC MARK : "))
Z=int(input("ENTER THE CHEMISTRY MARK : "))
A=X+Y+Z
if A<=300 :
    B=A*100/300
    if B>50 :
       print("PERCANTEGE : ",B)
       print("PASS")
    else :
        print("PERCANTEGE : ",B)
        print("FAIL")
else :
    print("NUMBERS ARE WRONG")
    
   
