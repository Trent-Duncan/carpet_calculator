# Trent Duncan
# 10/11/24
# carpet calculator



# Input

length=float (input("Please insert the Length of the room in feet \n"))
width=float (input("Please insert the Width of the room in feet \n"))
price_per_sq_yard=float (input("Please enter the price per square yard \n"))



# PROCESS
area= length*width
sq_yard= area/9
subtotal= sq_yard * price_per_sq_yard
sales_tax_rate= 0.06
sales_tax= subtotal * sales_tax_rate
grand_total= subtotal + sales_tax
# OUTPUT 
print(f"Your subtotal is: ${subtotal:.2f}")
print(f"You will need {sq_yard:.2f} sq yards")

print(f"You will pay ${sales_tax:.2f} in state sales tax.")

print(f"your grand total is: ${grand_total:.2f}")