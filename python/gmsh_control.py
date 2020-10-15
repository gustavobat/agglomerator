import pygmsh as gmsh
import numpy as np
import meshio
import os

geom = gmsh.built_in.Geometry()

# Draw a box
side_lenght = 0.4
poly = geom.add_box(0, side_lenght, 0, side_lenght, 0, side_lenght, lcar=0.02)

mesh = gmsh.generate_mesh(geom)

meshio.write("test.vtk", mesh)

os.system('paraview test.vtk &')
