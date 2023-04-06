import numpy as np
import astropy.units as u
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body, CartesianRepresentation
import pythreejs as p3j

# Set up the scene
scene = p3j.Scene()
renderer = p3j.Renderer(scene=scene, camera=p3j.PerspectiveCamera(position=[0, 0, 2e11]))
controller = p3j.OrbitControls(controlling=renderer.camera, target=[0, 0, 0])

# Set up the solar system
bodies = ["sun", "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune"]
colors = ["#fff200", "#8a8a8a", "#f4b942", "#1e90ff", "#ff0000", "#ba9653", "#ffc560", "#77c9d4", "#384dff"]
sizes = [15, 1.5, 3.5, 4, 2.5, 50, 40, 30, 25]

# Add each planet as a sphere to the scene
planets = []
for name, color, size in zip(bodies, colors, sizes):
    body = p3j.Mesh(
        p3j.SphereBufferGeometry(radius=size),
        p3j.MeshStandardMaterial(color=color),
        name=name
    )
    planets.append(body)
    scene.add(body)

# Define the time step and duration of the simulation
t = Time.now()
dt = 24 * u.hour
duration = 365 * u.day * 3  # 3 years

# Run the simulation
while t < Time.now() + duration:

    # Get the positions of each planet
    with solar_system_ephemeris.set("builtin"):
        positions = get_body(bodies, t).cartesian.xyz.to(u.m).value

    # Update the positions of each planet
    for planet, position in zip(planets, positions.T):
        planet.position = position

    # Render the scene
    renderer.render(scene)

    # Update the time
    t += dt
