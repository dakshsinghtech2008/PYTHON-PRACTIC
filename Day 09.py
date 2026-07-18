#Write a Python program that accepts an employee's salary and calculates the income tax according to these slabs:
# First ₹5,00,000 → 0%
# Next ₹5,00,000 → 10%
# Next ₹10,00,000 → 20%
# Remaining salary above ₹20,00,000 → 30%
# Finally, display the total tax.
salary = int(input("Enter your salary: "))
if salary <= 500000:
    tax = 0
elif salary <= 1000000:
    tax = (salary - 500000) * 0.10
elif salary <= 2000000:
    tax = (500000 * 0.10) + (salary - 1000000) * 0.20
else:
    tax = (500000 * 0.10) + (1000000 * 0.20) + (salary - 2000000) * 0.30
print("Tax =", tax)
