
#factorial of 5 = 5*4*3*2*1=120

n=int(input("enter the number"))
fact=1
for i in range (1,n+1):
    fact=fact*(i)
    print("the value of" ,n,"is:" ,fact)
