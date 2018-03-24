
# coding: utf-8

# In[22]:

import numpy as np
import pprint
get_ipython().magic('matplotlib notebook')


# In[17]:

data =  np.loadtxt('data.np')
print(data.shape)
data = data[100:200,100:200]
pprint.pprint(data)


# In[18]:

plt.imshow(data)
plt.show()


# In[4]:

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


# In[26]:

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.axes3d import Axes3D

x = np.arange(0,10,1)
y = np.arange(0,1,0.2)

xs, ys = np.meshgrid(np.arange(100), np.arange(100))
# z = calculate_R(xs, ys)
zs = xs**2 + ys**2

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(xs, ys, data, rstride=1, cstride=1, cmap='hot')
plt.show()


# In[ ]:



