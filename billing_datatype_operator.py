#Declaring
Product_Name="Shirt"
print("Product Name :",Product_Name)
print(type(Product_Name))

Product_Price=950.25
print("Product price :",Product_Price)
print(type(Product_Price))

Quantity=2
print("Quantity :",Quantity)
print(type(Quantity)) 

#Arithmetic Operators

Total_Price=Product_Price*Quantity
print("Total_Price :",Total_Price)
print(type(Total_Price))

Discount_Available=Total_Price>1500
print("Discount_Available :",Discount_Available)
print(type(Discount_Available))


if(Discount_Available==True) :
	Discount_Amount= (Product_Price * 10) / 100
	print("Discount_Amount :",Discount_Amount)
	print(type(Discount_Amount))
#Assignment Operators

Total_Price-=Discount_Amount
print("Total_Price :",Total_Price )

#Comparison Operators

print(Total_Price>1000)
print(Quantity==1)

#Logical Operators

print((Total_Price>500) and (Discount_Available==True))

#Display

Final_Bill=Total_Price
print("Final_Bill :",Final_Bill )
print(type(Final_Bill))
