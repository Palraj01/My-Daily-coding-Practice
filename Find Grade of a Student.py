#By giving the values

# n1=int(input("Enter the mark:"))
# n2=int(input("Enter the mark:"))
# n3=int(input("Enter the mark:"))
# avg=(n1+n2+n3)/3
# print(avg)
#
# if (avg>=90 and avg<100):
#     print("Grade A")
# elif (avg>=80 and avg<90):
#     print("Grade B")
# elif (avg>=70 and avg<80):
#     print("Grade C")
# elif(avg>=60 and avg<70):
#     print("Grade D")
# else:
#     print("fail")

#By Giving th inputs at the RUn time

n=int(input("Enter the number of subjects:"))
a=[]
for i in range(0,n):
    element=int(input("Enter the marks:"))
    a.append(element)
avg=sum(a)/n
print(avg)
if (avg>=90 and avg<100):
    print("Grade A")
elif (avg>=80 and avg<90):
    print("Grade B")
elif (avg>=70 and avg<80):
    print("Grade C")
elif(avg>=60 and avg<70):
    print("Grade D")
else:
    print("fail")
    