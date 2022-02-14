import numpy as np
import laspy as lp
import pptk

dataname="Baran.las"
point_cloud=lp.read(dataname)

points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()


v = pptk.viewer(points)
v.attributes(colors/65535)




