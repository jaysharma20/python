n=int(input("Enter the number"))
sum=0
order=len(str(n))
copy_n=n
while(n>0):
    digit=n%10
    sum+=digit**order
    n=n//10
if(sum==copy_n):
    print("Armstrong number")
else:
    print("Not an armstrong number")
