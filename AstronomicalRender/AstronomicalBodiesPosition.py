'''
astronomicalBodiesPosition.py - a program to display the astronomical bodies in a 3D enviroment. 
Name: Thomas Jordan
Last Modified: April 4, 2023
Version: 4.6
'''

import pyvista
from pyvista import examples

# ====================== SETUP 3D RENDER ======================
# Light of the Sun.
light = pyvista.Light()
light.set_direction_angle(30, -20)

# Load satellite
sat_filename = '/Users/Thomas/Documents/CPSC_Courses/GCI/AsteroidMitigation/sat.stl'
satellite = pyvista.read(sat_filename)

# Load planets
earth = examples.planets.load_earth(radius=6378.1)
jupiter = examples.planets.load_jupiter(radius=71492.0)
asteroid = examples.planets.load_pluto(radius=100.0)
satellite.scale([100.0, 100.0, 100.0], inplace=True)

# =================== Function Definition ===================

def moveAstronomicalBodies(body, x, y, z):
    body.translate((x, y, z), inplace=True)

# TODO: Ray Trace from satellite to asteroid 

# ====================== PLOT 3D RENDER ======================

# Setup space enviroment.
pl = pyvista.Plotter(lighting="none")
cubemap = examples.download_cubemap_space_16k()
pl.add_actor(cubemap.to_skybox())
pl.set_environment_texture(cubemap, True)
pl.add_light(light)

pl.add_mesh(earth, smooth_shading=True)
pl.add_mesh(jupiter, smooth_shading=True)
pl.add_mesh(satellite, smooth_shading=True)
