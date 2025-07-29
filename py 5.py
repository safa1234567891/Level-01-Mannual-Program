print("SAFA International [p] ltd")
print("No,15 Anna Nagar, Chennai")
print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Employee Payroll System")
print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
id=int(input("Enter the employee id:"))
name=input("Enter the employee name:")
salary=int(input("Enter the salary:"))
print("INCOME")
bonus=salary*20/100
print("Bonus 20% is :",bonus)
ot=salary*10/100
print("overtime 10% is:",ot)
ta=salary*5/100
print("Travel Allowance 5% is:",ta)
gpay=salary+ot+ta+bonus
print("Grosspay in Rupees:",gpay)
