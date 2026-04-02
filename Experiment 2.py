import math
import random
import matplotlib.pyplot as plt

k = "null"
arrA = [[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k]]
arrB = [[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k]]
arrV = [[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k]]
a = -1
b = -1
x=8
e = 1
kset = []
dset = []

def CostA(x,y):
    ans = x**y - 1
    return ans
def CostB(x,y):
    ans = x**y - 1
    return ans
for g in range(0,100):
    basea = random.uniform(1,2.5)
    for h in range(0,100):
        baseb = random.uniform(1,2.5)
        for m in range (0,x+1):
            for n in range (0,x+1):
                v = 2*m + 3*n
                at = v-CostA(basea,m)
                bt = v-CostB(baseb,n)
                arrV[m][n] = v
                arrA[m][n] = at
                arrB[m][n] = bt
        amax = ["null","null","null","null","null","null","null","null","null"]
        amin = "null"

        for i in range(0,x+1):
            amin = arrA[i][0]
            for j in range (0,x+1):
                temp = arrA[i][j]
                if amin > temp:
                    amin = temp
            amax[i] = amin

        avalue = amax[0]
        for element in amax:
            if avalue < element:
                avalue = element
        counter = 0
        temp = avalue 
        a = avalue
        for i in range (0,x+1):
            if avalue == amax[i]:
                counter = counter + 1
                a = a + i
        a = a - temp
        a = a/counter
        print(basea , " ", baseb)
        print(a)

        # b: optimal strategy for Person B now
        bmax = ["null","null","null","null","null","null","null","null","null"]
        bmin = "null"

        for j in range(0,x+1):
            bmin = arrB[0][j]
            for i in range (0,x+1):
                temp = arrB[i][j]
                if bmin > temp:
                    bmin = temp
            bmax[j] = bmin

        bvalue = bmax[0]
        for element in bmax:
            if bvalue < element:
                bvalue = element
        counter = 0
        temp = bvalue 
        b = bvalue
        for j in range (0,x+1):
            if bvalue == bmax[j]:
                counter = counter + 1
                b = b + i
        b = b - temp
        b = b/counter
        print(b)
        #find k
        gamma = 2*a + 3*b
        try:
            k = (2*a)/gamma - 0.5
        except:
            k = 0
        d = g-h
        point = (d,k)
        kset.append(k)
        dset.append(d)
        plt.plot(d,k,'.')
plt.title("Efficiency Differences on Free-Riding Behavior Graph")
plt.xlabel("Efficiency Differences")
plt.ylabel("Free-Riding Index")
plt.show()
#print(kset)
#print(dset)
