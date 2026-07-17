#INPUT 3 NUMBERS AND FIND THE GREATER NUMBER
x = int(input("ENTER THE FRIST NUMBER : "))
y = int(input("ENTER THE SECOND NUMBER : "))
z = int(input("ENTER THE THIRD NUMDER : "))

if x > y and x > z:
  print("Greater =", x)
elif y > x and y > z:
  print("Greater =", y)
elif z>x and z>y :
  print("Greater =", z)
else :
  print("ALL NUMBERS ARE EQUAL")
