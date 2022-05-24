num=int(input("Enter the number"))
sum=0
while(num>0):
    remainder=num%10
    sum=sum+remainder
    num=num//10
print("Sum of the digits of given num=%d"%sum)
