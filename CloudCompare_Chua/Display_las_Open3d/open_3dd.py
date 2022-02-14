import numpy as np
import laspy as lp
import open3d as o3d

dataname="Baran.las"
point_cloud=lp.read(dataname)

points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()


pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors/65535)
o3d.visualization.draw_geometries([pcd])


