import numpy as np
from mayavi import mlab 

arr_K_H = np.load('K_H.npy')
arr_K_G = np.load('K_G.npy')
arr_K1 = np.load('K1.npy')
arr_K2 = np.load('K2.npy')
vertices = np.load('vertices.npy')
triangles = np.load('triangles.npy')


mlab.figure('K_G')
mesh = mlab.triangular_mesh(vertices[:,0], vertices[:,1], vertices[:,2], triangles, representation='wireframe', opacity=0) 
mesh.mlab_source.dataset.point_data.scalars = arr_K_G 
mesh.mlab_source.dataset.point_data.scalars.name = 'Point data' 
mesh.mlab_source.update() 
mesh.parent.update()

mesh2 = mlab.pipeline.set_active_attribute(mesh, 
                point_scalars='Point data') 
s2 = mlab.pipeline.surface(mesh2)
s2.actor.mapper.interpolate_scalars_before_mapping = True

mlab.savefig(filename='K_G.png')
mlab.show()

mlab.figure('K_H')
mesh = mlab.triangular_mesh(vertices[:,0], vertices[:,1], vertices[:,2], triangles, representation='wireframe', opacity=0) 
mesh.mlab_source.dataset.point_data.scalars = arr_K_H 
mesh.mlab_source.dataset.point_data.scalars.name = 'Point data' 
mesh.mlab_source.update() 
mesh.parent.update()

mesh2 = mlab.pipeline.set_active_attribute(mesh, 
                point_scalars='Point data') 
s2 = mlab.pipeline.surface(mesh2) 
s2.actor.mapper.interpolate_scalars_before_mapping = True

mlab.savefig(filename='K_H.png')
mlab.show()

mlab.figure('K1')
mesh = mlab.triangular_mesh(vertices[:,0], vertices[:,1], vertices[:,2], triangles, representation='wireframe', opacity=0) 
mesh.mlab_source.dataset.point_data.scalars = arr_K1 
mesh.mlab_source.dataset.point_data.scalars.name = 'Point data' 
mesh.mlab_source.update() 
mesh.parent.update()

mesh2 = mlab.pipeline.set_active_attribute(mesh, 
                point_scalars='Point data') 
s2 = mlab.pipeline.surface(mesh2)
s2.actor.mapper.interpolate_scalars_before_mapping = True

mlab.savefig(filename='K1.png')
mlab.show()

mlab.figure('K2')
mesh = mlab.triangular_mesh(vertices[:,0], vertices[:,1], vertices[:,2], triangles, representation='wireframe', opacity=0) 
mesh.mlab_source.dataset.point_data.scalars = arr_K2
mesh.mlab_source.dataset.point_data.scalars.name = 'Point data' 
mesh.mlab_source.update() 
mesh.parent.update()

mesh2 = mlab.pipeline.set_active_attribute(mesh, 
                point_scalars='Point data') 
s2 = mlab.pipeline.surface(mesh2)
s2.actor.mapper.interpolate_scalars_before_mapping = True

mlab.savefig(filename='K2.png')
mlab.show()