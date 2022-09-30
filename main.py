import matplotlib.pyplot as plt
import numpy as np
from random import randint

x=randint(1,1000)
n=0
l=[]
a = x

while n<1000:
    if (a!=1):
        if (a%2==0):
            a=a/2
            l.append(a)
            n+=1
            if (a == 1):
                break
        if(a%2!=0):
            a=3*a+1
            l.append(a)
            n+=1
            if(a==1):
                break

print("\nRandom no. =",x)
print("No. of iteration =",len(l))
print("Largest no. =",max(l))

plt.plot(range(len(l)),l,color='r',linestyle='solid')
plt.title('The Collatz Conjucture')
plt.xlabel('Number of iteration(n)')
plt.ylabel('Conjucuture progression()')
plt.legend(['Value progression'])
plt.grid(True)
plt.show()
