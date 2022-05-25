


def perfect(x):
    s=0
    for i in range(1,x):
        if x%i==0:
            s=s+i
        return s
a=int(input("Enter the number:"))
r=perfect(a)
if(r==a):
    print("Perfect number")
else:
    print("Not a perfect number")

