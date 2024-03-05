
num=int(input("Enter the value:"))

if num<0:
    print("Enter the positive number")
else:
    value=0
    while(num>0):
        value=value+num
        num=num-1
print("the sum is:", value)

