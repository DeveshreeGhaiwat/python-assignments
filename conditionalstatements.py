"""##ifelse
a=int(input("enter the age"))
if(a>=18):
    print("eligible to vote")
else:
    print("not eligible to vote")"""




"""#while loop to print * pattern.
row=int(input("enter the number: "))
i=0
while(i<row):
    j=0
    while(j<=i):
        print("*",end=" ")
        j=j+1
    print()
    i=i+1

#Inverse pattern
row=int(input("enter the number: "))
i=row
while(i>=1):
    j=1
    while(j<=i):
        print("*",end=" ")
        j+=1
    print()
    i-=1
    
print("hardik",end=' ')
print("Pandya",end=' ')"""




#FOR LOOP 
rows=int(input("enter the number: "))
for i in range(0,rows) :
    for j in range(0,i+1):
        print("savi",end=" ")
    print()

"""#inverse
for i in range(5,0,-1):
    for j in range(i):
        print("",end=" ")   
    print()"""
   
