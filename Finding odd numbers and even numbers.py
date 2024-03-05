#Method : 1
# start=10
# end=20
#
# for i in range (start,end+1):
#     if (i%2==0):
#         print("the given number is even:" , i)
#     else:
#         print("the given number is odd:" , i)
#
#method : 2

n1=int(input("Enter the number:"))
n2=int(input("Enter the number:"))

for i in range (n1,n2+1):
    if (i%2==0):
        print("the given number is even:", i)
    else:
        print("the given number is odd:", i)

#method : 03 By printing the values in list format

n1 = int(input("Enter the number:"))
n2 = int(input("Enter the number:"))

for i in range(n1, n2 + 1):
    if (i % 2 == 0):
        print("the given number is even:", i)
    else:
        print("the given number is odd:", i)
