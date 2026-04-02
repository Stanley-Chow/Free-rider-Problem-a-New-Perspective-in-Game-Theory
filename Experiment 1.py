import random
import math
import matplotlib.pyplot as plt
import pandas
k = "null"
arrA = [[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k]]
arrB = [[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k]]
arrV = [[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k],[k,k,k,k,k,k,k,k,k]]
a = -1
b = -1
x=8
t = math.e
kset = []
dset = []
gset = []
hset = []

def CostA(m,a):
    ans = a**m - 1
    return ans
def CostB(n,b):
    ans = b**n - 1
    return ans

e1list = []
e2list = []

for p in range (0,100):
    temp = random.randint(0,1000)
    e1list.append(temp)
for p in range (0,100):
    temp = random.randint(0,1000)
    e2list.append(temp)

# Generator: fill in the matrices V,A,B
for g in e1list:
    e1 = g
    for h in e2list:
        e2 = h
        for m in range (0,x+1):
            for n in range (0,x+1):
                v = e1*m + e2*n
                a = v - CostA(m,t)
                b = v - CostB(n,t)
                arrV[m][n] = v
                arrA[m][n] = a
                arrB[m][n] = b

        #the following is the founder of nash equilibrium
        # a: optimal strategy for Person A now
        amax = ["null","null","null","null","null","null","null","null","null"]
        amin = "null"
        #print (arrV)

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
                b = b + j
        b = b - temp
        b = b/counter
        
        #find k
        gamma = e1*a + e2*b
        try:
            k = math.log((e1*a)/gamma - 0.5,math.e)
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
'''
sumk = 0
for p in range(len(kset)):
    sumk = sumk + kset[p]
meank = sumk/(len(kset))

sumd = 0
for q in range(len(dset)):
    sumd = sumd + dset[q]
meand = sumd/(len(dset))

dsamplevariance = 0
temp = 0
for p in range (len(dset)):
    temp = temp + (dset[p]-meand)**2
dsamplevariance = temp/(len(dset)-1)

ksamplevariance = 0
temp = 0
for q in range (len(kset)):
    temp = temp + (kset[q]-meank)**2
dsamplevariance = temp/(len(kset)-1)

covariance = 0
temp = 0
for r in range (len(dset)):
    temp = temp + (kset[r]-meank)*(dset[r]-meand)
covariance = temp/(len(dset)-1)

correlation = covariance / (dsamplevariance*ksamplevariance)**0.5

print("covariance is:", covariance)
print("sample variance of k is:", ksamplevariance)
print("sample variance of d is:", dsamplevariance)
print("mean k is:", meank)
print("mean d is:", meand)
print("correlation is,", correlation)
'''


dataset = {
    "d":dset,
    "k":kset
}
df = pandas.DataFrame(dataset)
print(df.corr())
