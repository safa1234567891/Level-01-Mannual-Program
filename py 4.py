print("AASHIFA SUPER MARKET")
print("No 44,NEHRU STREET,TINDIVNAM")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("BILL RECEIPT")
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
serial_no=int(input("Enter the serial no :"))
part=input("Enter the particular:")
rate=int(input("Enter the rate:"))
qty=int(input("Enter the quantity:"))
total=rate*qty
print("Total Amount:",total)
gst=total*10/100
print("GST 10% is :",gst)
paid=total+gst
print("Amount to be paid Rs:",paid)
