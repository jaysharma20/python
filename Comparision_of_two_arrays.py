import numpy as np
a=np.array([1,2,3,4,5,6])
b=np.array([1,2,3,4,5,7])
c=a==b
print(c)
print(any(c))
print(all(c))
