a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
c=int(input("Enter the value:"))

#semi perimeter=s
s=(a+b+c)/2
print("semi perimeter:",s)

Area=(s*(s-a)*(s-b)*(s-c))**0.5
print("Area of the triangle sides",a,b,c ,"is:" ,Area)


