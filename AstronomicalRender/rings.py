'''
rings.py - file to handle ring rotation, orbit, and gravity
Name: Thomas Jordan
Last Modified: April 20, 2023
Version: 1.3
'''

from vpython import extrusion, shapes, vector

class PlanetRing:
    def __init__(self, outerRadius, innderRadius, planet, ring_height, mass, planet_scale, color):
        try:
            self.outerRadius = outerRadius * planet_scale
            self.innerRadius = innderRadius * planet_scale
            self.planet = planet
            self.ring_height = ring_height * planet_scale
            self.mass = mass
            self.planet_scale = planet_scale
            self.color = color


            # Rings are at most, 1 km thick

            # Create Saturn's rings using extrusion
            ring_path = [vector(0, 0, 0), vector(0, self.ring_height, 0)]
            ring_shape = shapes.circle(radius=self.outerRadius, thickness=self.outerRadius - self.innerRadius)
            self.obj = extrusion(path=ring_path, 
                                 shape=ring_shape, 
                                 pos=self.planet.obj.pos, 
                                 color = self.color)
     
        except TypeError:
            print("TypeError: wrong arguments type!!")
        except ZeroDivisionError:
            print("ERROR: Rotation period and orbital period can't be zero")


    def rotate_orbit(self):
        """Method that keeps rings aligned with planet"""
        try:
            '''Rotates at different speed'''
            self.obj.pos = self.planet.obj.pos

        except ZeroDivisionError:
            print("ERROR: REFRESH_RATE is 0")
        except (AttributeError, TypeError):
            print("ERROR: wrong arguments type while initializing!!")
