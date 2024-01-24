
def additem(products,productname,productprice):
    products.append((productname,productprice))
for i in range(2):
    productname=input("enter the product name: ")
    productprice=int(input("enter the product price: "))
    additem(products,productname,productprice)
print(products)

total = sum(products)
print(total)
 


