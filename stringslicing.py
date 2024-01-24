"""#string slicing
"samay"
for x in "samay":
    print(x)
a="string length"
print(len(a))
print("length" in a)
print("sky" in a)
print("sky" not in a)
print(a[3:6])

b="smeartactics"
print(b[-9:-6])
print(b[3:6])
print(b[5:])
print(b[:5])
print(b[0:7:3])

#string modifications
c="   Smear Tactics   "
print(c)
print(c.lower())
print(a+b)
print(("hello"+c))"""

print("hardikPandya")
a="Hardik Pandya"
print(a[0])
print(a[5:])
print(a.lower())
print(a.title())
print(a.swapcase())
print(a.casefold())
print(a.center(10))
print(a.count("d"))
print(a.index("r"))
print(a.encode(encoding="ascii"))
print(a.endswith("a"))
print(a.isdigit())
print(a.isalpha())
print(a.isnumeric())
print(a.isdecimal())
print(a.replace("Hardik","krunal"))


#format
d="My name is {name} and I am {age} years old"
print(d.format(name="savi",age=19))
print(d.find("i"))






