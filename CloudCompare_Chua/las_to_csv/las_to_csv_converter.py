#this code and las file need to be put in directory
#~/anaconda3/envs/CloudComPy39/doc/PythonAPI_test

# run these commands before run this code
'''
. ~/anaconda3/etc/profile.d/conda.sh
conda activate CloudComPy39
export LD_LIBRARY_PATH=~/anaconda3/envs/CloudComPy39/lib:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=~/anaconda3/envs/CloudComPy39/lib/cloudcompare:${LD_LIBRARY_PATH}
export LD_LIBRARY_PATH=~/anaconda3/envs/CloudComPy39/lib/cloudcompare/plugins:${LD_LIBRARY_PATH}
cd ~/anaconda3/envs/CloudComPy39/doc/PythonAPI_test
ctest
. envPyCC.sh
'''

import cloudComPy as cc                                                # import the CloudComPy module
cc.initCC()                                                            # to do once before dealing with plugins

cloud = cc.loadPointCloud("Baran.las")                               # read a point cloud from a file
print("cloud name: %s"%cloud.getName())

res=cc.computeCurvature(cc.CurvatureType.GAUSSIAN_CURV, 0.05, [cloud]) # compute curvature as a scalar field
nsf = cloud.getNumberOfScalarFields()
sfCurv=cloud.getScalarField(nsf-1)
cloud.setCurrentOutScalarField(nsf-1)
filteredCloud=cc.filterBySFValue(0.01, sfCurv.getMax(), cloud)         # keep only the points above a given curvature

ok = filteredCloud.exportCoordToSF(False, False, True)                 # Z coordinate as a scalar Field
nsf = cloud.getNumberOfScalarFields()
sf1=filteredCloud.getScalarField(nsf-1)
mean, var = sf1.computeMeanAndVariance()

# using Numpy...

coordinates = filteredCloud.toNpArrayCopy()                            # coordinates as a numpy array
x=coordinates[:,0]                                                     # x column
y=coordinates[:,1]
z=coordinates[:,2]

f=(2*x-y)*(x+3*y)                                                      # elementwise operation on arrays

asf1=sf1.toNpArray()                                                   # scalar field as a numpy array
sf1.fromNpArrayCopy(f)                                                 # replace scalar field values by a numpy array

res=cc.SavePointCloud(filteredCloud,"Baran.csv")             #save the point cloud to a file
