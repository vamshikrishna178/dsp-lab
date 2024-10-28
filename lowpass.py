
import numpy as np
import matplotlib.pyplot as plt
fs=int(input("enter the sampled freaquesny"))
n=int(input("enter the number of dft pointer"))
fc=int(input("entert the cut off frequency which should be less than half of the sampled frequency"))
a=fs/2
F=[]
x=0
lpf=[]
hpf=[]
graph=[]
for k in range(0,int(n)):
	x=(fs/n)*k
	if(x<=a):
		F.append(x)
	else:
		F.append(a-(x-a))
print("F",F)
for b in range(0,int(n)):
	if(F[b]<=fc):
		lpf.append(1)
	else:
		lpf.append(0)
print("lpf",lpf)
for b in range(0,int(n)):
	if(F[b]>=fc):
		hpf.append(1)
	else:
		hpf.append(0)
print("hpf",hpf)
plt.subplot(2,1,1)
plt.stem(lpf)
plt.subplot(2,1,2)
plt.stem(hpf)
plt.show()




