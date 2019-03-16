import math

x=[]

a=int(input())

for i in range(a):
    x.append(int(input()))


print(x)



for i in x:
    s=0
    s=s+(i*i)

rms=math.sqrt(s/len(x))


print(rms)


