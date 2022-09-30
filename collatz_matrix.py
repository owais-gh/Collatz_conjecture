import matplotlib.pyplot as plt
import numpy as np
from random import randint

x,n=2,0
l,xl=[],[]
iv=0

while x<1000:
    a =x
    while n<1000:
        if (a%2==0):
            a=a/2
            l.append(a)
            xl.append(x)
            n+=1
            if (a == 1):
                break
        if(a%2!=0):
            a=3*a+1
            l.append(a)
            xl.append(x)
            n+=1
            if(a==1):
                break
    x+=1
    xl.append(x)




print("\nRandom no. = ",x)
print("No. of iteration = ",len(l))
print("Largest no. = ",max(l))
print(len(xl),'and',len(l))

for z in xl :
    plt.plot(range(len(l)),l,color='r',linestyle='solid')


plt.title('The Collatz Conjucture')
plt.xlabel('Number of iteration(n)')
plt.ylabel('Conjucuture progression()')
plt.legend(['Value progression'])
plt.grid(True)
plt.show()
