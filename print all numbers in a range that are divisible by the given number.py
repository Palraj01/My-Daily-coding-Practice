#Directly entering the values
# start=10
# end=20
# number=2
# for i in range (start,end+1):
#     if (i%2==0):
#         print(i)

# BY giving the I/P at the run time

start=int(input("Enter a number:"))
end=int(input("Enter a number:"))
number=int(input("Enter a number to be divided:"))

for i in range (start,end+1):
    if (i%number==0):
        print(i)

