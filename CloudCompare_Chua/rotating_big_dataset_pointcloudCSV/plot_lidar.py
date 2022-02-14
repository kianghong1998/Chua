from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import pandas as pd

file_str = input("Open what file:")

data_col =['x','y','z','r','g','b','xx','yy']
data = pd.read_csv(file_str, delim_whitespace=True, names=data_col)
print (data)

x,y,z = data ['x'], data ['y'], data ['z']

fig = plt.figure()

ax = Axes3D(fig)
plt.plot(x, y, z, marker='.', markersize=1, lw=0)

ax.set_title("Cloud")
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()


