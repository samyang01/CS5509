# Create linear regression model for the following table using numpy only.
# Plot the model using matplotlib

import numpy as np
import matplotlib.pyplot as plt

x_array = np.arange(10)
y_array = np.array([1,3,2,5,7,8,8,9,10,12])
z = np.polyfit(x_array,y_array, 1)
f=np.poly1d(z)
##############################
x_mean=np.mean(x_array)
y_mean=np.mean(y_array)

b0=0
b1=0
for i in range(10):
    b0+=(x_array[i]-x_mean)*(y_array[i]-y_mean)
    b1+=(x_array[i]-x_mean)**2

b2=b0/b1
b3 = y_mean-b2*x_mean

print(b0/b1)
print(b3)
#############################
print(f)

x_new=np.linspace(0,10,50)
y_new=f(x_new)

plt.plot(x_array,y_array,'o',x_new,y_new)
plt.show()