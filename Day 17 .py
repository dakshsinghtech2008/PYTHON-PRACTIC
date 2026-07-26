#Write a Python program to input the MRP and quantity of two products. 
#Calculate the total bill of each product and find which product's bill is higher. 
#Also calculate by what percentage the higher bill is greater than the lower bill.

ra = int(input("ENTER THE MRP OF PRODUCT 1 : "))
qua = int(input("ENTER THE QUANTITY OF PRODUCT 1 : "))
F1 = ra * qua
print("TOTAL BILL OF PRODUCT 1 :", F1)

rat = int(input("ENTER THE MRP OF PRODUCT 2 : "))
quan = int(input("ENTER THE QUANTITY OF PRODUCT 2 : "))
F2 = rat * quan
print("TOTAL BILL OF PRODUCT 2 :", F2)

if F1 > F2:
    per = (F1 - F2) * 100 / F2
    print("PRODUCT 1 BILL MORE PERCANTEGE % : ", per)
elif F2 > F1:
    per = (F2 - F1) * 100 / F1
    print("PRODUCT 2 BILL MORE PERCANTEGE % : ", per)
else:
    print("BOTH BILLS ARE EQUAL")
