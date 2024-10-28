import numpy as np

x1 = [1,2,3,4]
x2 = [-1,0,5,3]
N = len(x1)

def cyclic_delay(x, m):
	y = []
	for n in range(0, N):
		if n-m >= 0:
			idx = n-m%N
		else: 
			idx = N+n-m
		y.append(x1[idx])
	return y

def cyclic_convolution(x1, x2):
    z = []
    a = x2[::-1]
    
    for n in range(N):
        y =np.roll(x2_r, n)
        z.append(np.dot(x1, y))  
    return z

# Compute the cyclic convolution
Y = cyclic_convolution(x1, x2)
print("Cyclic Convolution Result:", Y)
