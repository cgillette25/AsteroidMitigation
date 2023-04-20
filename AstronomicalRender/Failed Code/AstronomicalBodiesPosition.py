'''
astronomicalBodiesPosition.py - a program to display the astronomical bodies in a 3D enviroment. 
Name: Thomas Jordan
Last Modified: April 4, 2023
Version: 4.6
'''
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

'''

# Setup 3D Enviroment 
from vpython import *

scene.width = scene.height = 600

# Display text below the 3D graphics:
scene.title = "Asteroid Mitigation using Lasers"

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

Nstars = 20  # change this to have more or fewer stars

G = 6.7e-11 # Universal gravitational constant

# Typical values
Msun = 2E30
Rsun = 2E9
L = 4e10
vsun = 0.8*sqrt(G*Msun/Rsun)

scene.range = 2*L
scene.forward = vec(-1,-1,-1)

xaxis = curve(color=color.gray(0.5), radius=3e8)
xaxis.append(vec(0,0,0))
xaxis.append(vec(L,0,0))
yaxis = curve(color=color.gray(0.5), radius=3e8)
yaxis.append(vec(0,0,0))
yaxis.append(vec(0,L,0))
zaxis = curve(color=color.gray(0.5), radius=3e8)
zaxis.append(vec(0,0,0))
zaxis.append(vec(0,0,L))

Stars = []
star_colors = [color.red, color.green, color.blue,
              color.yellow, color.cyan, color.magenta]

psum = vec(0,0,0)
for i in range(Nstars):
    star = sphere(pos=L*vec.random(), make_trail=True, retain=150, trail_radius=2e8)
    R = Rsun/2+Rsun*random()
    star.radius = R
    star.mass = Msun*(R/Rsun)**3
    star.momentum = vec.random()*vsun*star.mass
    star.color = star.trail_color = star_colors[i % 6]
    Stars.append( star )
    psum = psum + star.momentum

#make total initial momentum equal zero
for i in range(Nstars):
    Stars[i].momentum = Stars[i].momentum - psum/Nstars

dt = 1000
hitlist = []

def computeForces():
    global hitlist, Stars
    hitlist = []
    N = len(Stars)
    for i in range(N):
        si = Stars[i]
        if si is None: continue
        F = vec(0,0,0)
        pos1 = si.pos
        m1 = si.mass
        radius = si.radius
        for j in range(N):
            if i == j: continue
            sj = Stars[j]
            if sj is None: continue
            r = sj.pos - pos1
            rmag2 = mag2(r)
            if rmag2 <= (radius+sj.radius)**2: hitlist.append([i,j])
            F = F + (G*m1*sj.mass/(rmag2**1.5))*r
        si.momentum = si.momentum + F*dt

while True:
    rate(100)
    
    # Compute all forces on all stars
    computeForces()

    # Having updated all momenta, now update all positions
    for star in Stars:
        if star is None: continue
        star.pos = star.pos + star.momentum*(dt/star.mass)

    # If any collisions took place, merge those stars
    hit = len(hitlist)-1
    while hit > 0:
        s1 = Stars[hitlist[hit][0]]
        s2 = Stars[hitlist[hit][1]]
        if (s1 is None) or (s2 is None): continue
    
        mass = s1.mass + s2.mass
        momentum = s1.momentum + s2.momentum
        pos = (s1.mass*s1.pos + s2.mass*s2.pos) / mass
        s1.color = s1.trail_color = (s1.mass*s1.color + s2.mass*s2.color) / mass
        R = Rsun*(mass / Msun)**(1/3)
        
        s1.clear_trail()
        s2.clear_trail()
        s2.visible = False
        
        s1.mass = mass
        s1.momentum = momentum
        s1.pos = pos
        s1.radius = R
        Stars[hitlist[hit][1]] = None
        hit -= 1
