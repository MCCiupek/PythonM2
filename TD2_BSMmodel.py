import numpy as np

# my_matrix = [None] * 100000
# print(len(my_matrix))

# my_matrix_2 = np.empty([2,2],dtype)

S0 = 100
K = 105
T = 1
r = 0.05
v = 0.2
I = 1000

z = np.random.standard_normal(I)

ST = S0*np.exp((r - 0.5*v**2)*T+v*np.sqrt(T)*z)
hT = np.max(ST-K,0)
C = np.exp(-r*T)*1/I*np.sum(hT)
print("Call Value : {0,1.4f}", C*100, "%")