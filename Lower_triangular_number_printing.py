n=int(input("Enter the value of n:\n"))
c=1
for i in range(1,n+1):
  for j in range(i):
    print(c,end="")
    if c<9:
      c+=1
    else:
      c=1
  print()
