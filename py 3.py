print("Goverment of tamilnadu")
print("Electricity Board")
print("_ _ _ _ _ _ _ _ _ _ _ _")
no=input("Enter a EB No:")
name=input("Reading for customer name:")
prev=int(input("Reading for previous month:"))
cur=int(input("Reading for current month:"))
Total=cur-prev
print("Total unit consumed:",Total)
Paid=Total*5
print("Amount to be paid:",Paid)
