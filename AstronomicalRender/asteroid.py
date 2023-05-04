'''
planet.py - file to handle planet rotation, orbit, and gravity
Name: Thomas Jordan
Last Modified: April 19, 2023
Version: 12.1
'''

from vpython import sphere, vector, pi
from math import sin, cos, sqrt, atan2

class Asteroid:
    def __init__(self, diameter, distance_to_sun, rotation_period_in_hours, orbital_period_in_days, texture, mass,
                 inclination_angle, star, planet_scale, distance_scale, time_scale, refresh_rate):
        try:
            # Set attributes to object
            self.radius = diameter / 2.0
            self.distance_to_sun = distance_to_sun
            self.rotation_speed = 2.0 * pi / (rotation_period_in_hours * 3600)  # [rad/sec]
            self.orbit_speed = 2.0 * pi / (orbital_period_in_days * 3600 * 24)
            self.texture = texture
            self.mass = mass
            self.star = star
            self.planet_scale = planet_scale
            self.distance_scale = distance_scale
            self.time_scale = time_scale
            self.refresh_rate = refresh_rate
            self.inclination_angle = inclination_angle
            self.obj = sphere(radius=self.radius * self.planet_scale,
                              pos=vector(-self.distance_to_sun * self.distance_scale, 0, 0), texture=self.texture,
                              make_trail=False)
            self.sum_ang = 0
        except TypeError:
            print("TypeError: wrong arguments type!!")
        except ZeroDivisionError:
            print("ERROR: Rotation period and orbital period can't be zero")

    def update(self, time_scale):
        """This method is used to update time_scale which can be changed from outside this class"""
        self.time_scale = time_scale
        self.obj.interval = 1 / (self.orbit_speed * self.time_scale)

    def rotate_axis(self):
        """Method that rotates planet"""
        try:
            # Venus and Uranus rotate in the opposite direction as earth
            if (self == 'uranus' or self == 'venus'):
                self.obj.rotate(angle=self.rotation_speed * self.time_scale / self.refresh_rate, axis=vector(0, 1, 0))
            else:
                self.obj.rotate(angle=self.rotation_speed * self.time_scale / self.refresh_rate, axis=vector(0, 1, 0))
        except ZeroDivisionError:
            print("ERROR: REFRESH_RATE is 0")
        except (AttributeError, TypeError):
            print("ERROR: wrong arguments type while initializing!!")

    def rotate_orbit(self):
        """Method that orbits planet around a star"""
        try:
            '''
            # ang = self.inclination_angle
            # xy rotation component
            ang_xy = self.orbit_speed * self.time_scale / self.refresh_rate
            self.obj.rotate(angle=ang_xy, axis=vector(0, 1, 0), origin=self.star.obj.pos)
            self.sum_ang += ang_xy
            '''
            # Combine x, y, and z angles into a single vector using:
            # Cartesian and spherical coordinate systems
            # Reference: https://openstax.org/books/calculus-volume-3/pages/2-7-cylindrical-and-spherical-coordinates)

            ang = self.orbit_speed * self.time_scale / self.refresh_rate

            # Track how far along orbit planet is
            self.sum_ang += ang

            # Convert inclination angle to radians
            radians_inclination_angle = self.inclination_angle * (pi / 180)
            radians_xy_angle = ang * (pi / 180)

            # Find spherical coordinates
            rho = self.distance_to_sun
            theta = radians_xy_angle
            phi = radians_inclination_angle

            # Convert spherical coordinates into cartessian coordinates
            y = rho * sin(phi) * cos(theta)
            x = rho * cos(phi)
            z = rho * sin(phi) * sin(theta)

            # Rotate planet on tilted axis
            self.obj.rotate(angle=ang, axis=vector(x, y, z), origin=self.star.obj.pos)

        except ZeroDivisionError:
            print("ERROR: REFRESH_RATE is 0")
        except (AttributeError, TypeError):
            print("ERROR: wrong arguments type while initializing!!")


    def trail(self, trail_radius=0):
        """This method draws trail behind a planet (if you don't give any value to trail_radius, trail will resize
        when zooming in or out)"""
        try:
            if self.sum_ang > 2 * pi:
                self.obj.make_trail = False
            else:
                if trail_radius == 0:
                    self.obj.trail_radius = trail_radius
                self.obj.make_trail = True
        except AttributeError:
            print("ERROR: wrong arguments type while initializing!!")

    def clear_trail(self):
        """This method should be used when you want to no longer draw a trail and delete it"""
        self.obj.make_trail = False
        self.obj.clear_trail()
        self.sum_ang = 0
