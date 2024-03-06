
num=int(input("enter a number"))
n1,n2=0,1
count=0;

if num<0:
    print("Fibonacci series cannot be generated")
elif num==1:
    print("fibonacci series is num")
else:
    print("the fibonacci series is:")
    while count<num:
        print(n1)
        lastnum=n1+n2
        n1=n2
        n2=lastnum
        count+=1
