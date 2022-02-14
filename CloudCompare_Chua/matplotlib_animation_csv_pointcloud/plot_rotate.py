import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
 
data_col =['x','y','z','r','g','b']
data = pd.read_csv("cloud.csv", delim_whitespace=True, names=data_col)
print (data)
  
# THE DATA POINTS
x = data['x']
y = data['y']
z = data['z']
dataSet = np.array([x, y, z])
numDataPoints = len(z)

fig = plt.figure()
ax = Axes3D(fig)
redDots = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=0, c='r', marker='.', markersize=1) # For scatter plot
 
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.set_title('pointcloud')
 
#rotate
for angle in range(0, 360):
    ax.view_init(30, angle)
    plt.draw()
    plt.pause(.001) 

