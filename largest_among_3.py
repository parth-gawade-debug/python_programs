# this program finds the largest number among the given 3 random numbers 
a=int(input("enter 1st number:"))
b=int(input("enter 2nd number:"))
c=int(input("enter 3rd number:"))

if (a>=b and a>=c):
    print("The largest number among the three is :",a)
elif(b>=c and b>=a):
    print("The largest number among the three is :",b)
else :
    print("The largest number among the three is :",c)
