import math
import matplotlib.pyplot as plt
import random
import pandas

def Cost (x,y):
    ans = (x**y) - 1
    return ans

x = 8
e1 = 3
e2 = 3
kset = []
dset = []

for i in range (0,1000):
    V = []
    A = []
    B = []
    baseA = random.uniform(1.1,2.5)
    baseB = random.uniform(1.1,2.5)
    for t in range (x+1):
        V.append(["null","null","null","null","null","null","null","null","null"])
        A.append(["null","null","null","null","null","null","null","null","null"])
        B.append(["null","null","null","null","null","null","null","null","null"])
    for m in range (0,x+1):
        for n in range (0,x+1):
            v = m*e1 + n*e2
            a = v - Cost(baseA,m)
            b = v - Cost(baseB,n)
            V[m][n] = v
            A[m][n] = a
            B[n][m] = b
    
    atemp = []
    alpha1 = 0
    counter = 0
    for m in range(0,x+1):
        temp = min(A[m])
        atemp.append(temp)
    anash = max(atemp)
    for m in range(0,x+1):
        temp = min(A[m])
        if temp == anash:
            alpha1 += m
            counter = counter + 1
    alpha = alpha1/counter

    btemp = []
    beta1 = 0
    counter = 0
    for n in range(0,x+1):
        temp = min(B[n])
        btemp.append(temp)
    bnash = max(btemp)
    for n in range(0,x+1):
        temp = min(B[n])
        if temp == bnash:
            beta1 += n 
            counter = counter + 1
    beta = beta1/counter
    
    
    gamma = e1*alpha + e2*beta
    try:
        k = (e1*alpha)/gamma -0.5
    except:
        k = 0
    kset.append(k)
    #d = math.log(baseA,math.e)-math.log(baseB,math.e)
    d = baseA - baseB
    dset.append(d)
    plt.plot(d,k,'.')

plt.title("Cost Function Differences on Free-Riding Behavior Graph")
plt.xlabel("Cost Function Differences")
plt.ylabel("Free-Riding Index")
plt.show()

dataset = {
    'd':dset,
    'k':kset
}

df=pandas.DataFrame(dataset)
corr = df.corr()
print(corr)