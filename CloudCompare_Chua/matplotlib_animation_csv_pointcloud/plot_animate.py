import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
 
data_col =['x','y','z','r','g','b']
data = pd.read_csv("cloud.csv", delim_whitespace=True, names=data_col)
print (data)
 
# ANIMATION FUNCTION
def func(num, dataSet, redDots): 
    redDots.set_data(dataSet[0:2, :num])    
    redDots.set_3d_properties(dataSet[2, :num]) 
    return redDots
 
 
# THE DATA POINTS
x = data['x']
y = data['y']
z = data['z']
dataSet = np.array([x, y, z])
numDataPoints = len(z)
 
fig = plt.figure()
ax = Axes3D(fig)
redDots = plt.plot(dataSet[0], dataSet[1], dataSet[2], lw=0, c='r', marker='.', markersize=1)[0] # For scatter plot
 
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Point Cloud')
 
# Creating the Animation object
anim = animation.FuncAnimation(fig, func, frames=numDataPoints, fargs=(dataSet, redDots), interval=1, blit=False)
 
plt.show()
