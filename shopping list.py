products=[]
def additem(products,productname,productprice):
 products.append((productname,productprice))
while(True):
  n=int(input("enter your choice:"))
  if(n==1):
    for i in range(2):
      productname=input("enter the product name: ")
      productprice=int(input("enter the product price: "))
      additem(products,productname,productprice)
    print(products)
  elif(n==2):
    for productsname,productprice in products:
      print(f"{productname}: ${productprice}")
  elif(n==3):
    sum_of_prices = sum(product[1] for product in products)
    print("Sum of product prices :", sum_of_prices)
  else:
    break



    


