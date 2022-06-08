import cloudComPy as cc
cc.initCC()

mesh = cc.loadMesh("/home/test/Downloads/test.obj")
pointcloud = mesh.samplePoints(False, 1000000)

cc.SavePointCloud(pointcloud, '/home/test/Downloads/test.bin')
