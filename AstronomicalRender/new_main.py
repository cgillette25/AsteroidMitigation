'''
main.py - main function for the frontend 3D enviroment
Name: Thomas Jordan
Last Modified: April 19, 2023
Version: 7.9
References:
    * https://iopscience.iop.org/article/10.1088/0004-637X/750/2/135/pdf
    * https://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/program/Stars-VPython
    * https://nssdc.gsfc.nasa.gov/planetary/factsheet/
    * https://github.com/Spartadays/SolarSystem
    * https://sps.nus.edu.sg/~chammika/workshops/2019_tfi_hanoi/restricted/vpython-code-for-the-earth-sun-system.html
    * https://thepythoncodingbook.com/2021/09/29/simulating-orbiting-planets-in-a-solar-system-using-python-orbiting-planets-series-1/
    * https://en.wikipedia.org/wiki/Orbital_inclination
    * https://guigui.developpez.com/cours/python/vpython/en/?page=workobject
    * https://openstax.org/books/calculus-volume-3/pages/2-7-cylindrical-and-spherical-coordinates
    * https://www.nasa.gov/sites/default/files/files/Distance_to_the_Moon.pdf
    * https://nssdc.gsfc.nasa.gov/planetary/factsheet/satringfact.html
    * https://www.science.org/doi/10.1126/science.aat2965
    * https://spacemath.gsfc.nasa.gov/weekly/10Page28.pdf
    * https://www.wionews.com/science/an-astronomer-has-created-video-on-saturns-spinning-rings-375558
    * https://solarsystem.nasa.gov/planets/saturn/in-depth/#:~:text=Saturn's%20ring%20system%20extends%20up,meters)%20in%20the%20main%20rings.
'''

try:
    import sys
    from vpython import *
    from sun import Star
    from planet import Planet
    from rings import PlanetRing
    from satellite import Satellite
    from moon import Moon
    from asteroid import Asteroid
    "from lagrange import Lagrange"

except ImportError as error:
    print("Error during loading module. {}".format(error))
    sys.exit(2)

# ======= Interactive Elements =======
def start_flag_button(b):
    """Function to start/stop animation (axis and orbit rotations)"""
    global start_flag
    start_flag = not start_flag
    if start_flag:
        b.text = "Pause"
    else:
        b.text = "<b>START</b>"

def time_scale_menu(m):
    """Function to set time_scale to selected from list menu"""
    global time_scale
    if m.selected == '1s = 1h':
        time_scale = 3600
    elif m.selected == '1s = 24h':
        time_scale = 3600 * 24
    elif m.selected == '1s = 30days':
        time_scale = 3600 * 24 * 30
    elif m.selected == '1s = 90days':
        time_scale = 3600 * 24 * 30 * 3
    elif m.selected == '1s = 180days':
        time_scale = 3600 * 24 * 30 * 6

def camera_menu(m):
    """This function position camera.center to selected object from list menu"""
    if m.selected in solar_system:
        scene.camera.follow(solar_system[m.selected].obj)

def trail_flag_button(b):
    """Function to set trail_flag value (T/F) taken from user"""
    global trail_flag
    trail_flag = not trail_flag
    if trail_flag:
        b.text = "trail is on"
    else:
        b.text = "trail is off"

# ============== MAIN ==============

if __name__ == '__main__':
    #PLANET_SCALE = 0.0001  # 0.0001
    PLANET_SCALE = 0.00002
    DISTANCE_SCALE = 0.0000002  # 0.0000002
    SUN_SCALE = 0.1 * PLANET_SCALE  # 0.1
    REFRESH_RATE = 120  # [how much per second]
    # On lower refresh rate you will not notice planet that is rotating very fast, or you can see it rotating slowly.
    # That's because of stroboscopic effect
    time_scale = 1 * 3600  # [sec]
    start_flag = False
    trail_flag = False

    # SCENE:
    #scene.visible = False # Show nothing until all assets are loaded

    scene = canvas(width=1200, height=700)
    scene.title = int(0.1 * scene.width) * ' ' + 'Asteroid Mitigation using Lasers\n',
    scene.ambient = color.gray(0.7)
    scene.autoscale = False
    scene.lights = []

    # Using deep space image: https://svs.gsfc.nasa.gov/4851
    # Converted to cubemap using: https://jaxry.github.io/panorama-to-cubemap/
    # Define the six images of the space cubemap
    '''
    textures = {
        "posx": "px.png",
        "negx": "nx.png",
        "posy": "py.png",
        "negy": "ny.png",
        "posz": "pz.png",
        "negz": "nz.png"
    }
    '''

    #scene.background = 'Cubemap/px.png'

    # SOLAR SYSTEM OBJECTS:
    # Units are in km
    # Data from: https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html,
    #            https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
    #            https://iopscience.iop.org/article/10.1088/0004-637X/750/2/135/pdf

    sun = Star(1392684,
                27 * 24,
                'new_textures/sun.jpg',
                1988500 * 10**24,
                time_scale,
                REFRESH_RATE,
                SUN_SCALE)

    mercury = Planet(4879,
                    57910000,
                    1407.6,
                    87.969,
                    'new_textures/mercury.jpg',
                    0.330 * 10**24,
                    7.0,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    venus = Planet(12104,
                    108200000,
                    -5832.5,
                    224.7,
                    'new_textures/venus.jpg',
                    4.87 * 10**24,
                    3.4,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    earth = Planet(12756,
                    149600000,
                    23.9,
                    365.25,
                    'new_textures/earth.jpg',
                    5.97 * 10**24,
                    0.0,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    asteroid = Asteroid(1275,
                    179600000,
                    999999,
                    365.25,
                    'new_textures/earth.jpg',
                    5.97 * 10**22,
                    30.0,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)

    lagrange = Planet(500,
                        151500000,
                        9999999999999999,
                        365.25,
                        'new_textures/neptune.jpg',
                        0,
                        0.0,
                        sun,
                        PLANET_SCALE,
                        DISTANCE_SCALE,
                        time_scale,
                        REFRESH_RATE)

    # https://www.nasa.gov/sites/default/files/files/Distance_to_the_Moon.pdf
    moon = Moon(3475,
                382500,
                655.7,
                27.3,
                'new_textures/moon.jpg',
                0.073 * 10**24,
                5.1,
                earth)

    satellite = Satellite(100,
                     500000,
                     9999999,
                     168,
                      'new_textures/moon.jpg',
                      0,
                      30,
                      lagrange)

    mars = Planet(6792,
                    227900000,
                    24.6,
                    68.7638,
                    'new_textures/mars.jpg',
                    0.642  * 10**24,
                    1.8,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    jupiter = Planet(142984,
                    778600000,
                    9.9,
                    11 * 365.25 + 315,
                    'new_textures/jupiter.jpg',
                    1898 * 10**24,
                    1.3,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    saturn = Planet(120536,
                    1433000000,
                    10.7,
                    29 * 365.25 + 167,
                    'new_textures/saturn.jpg',
                    568  * 10**24,
                    2.5,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    """lagrange = Lagrange(2000,
                        151100000,
                        365.25,
                        'new_textures/sun.jpg',
                        5.97 * 10**24, 0.0,
                        sun,
                        PLANET_SCALE,
                        DISTANCE_SCALE,
                        time_scale,
                        REFRESH_RATE)"""
    # https://nssdc.gsfc.nasa.gov/planetary/factsheet/satringfact.html
    # https://www.science.org/doi/10.1126/science.aat2965
    # https://spacemath.gsfc.nasa.gov/weekly/10Page28.pdf
    # https://www.wionews.com/science/an-astronomer-has-created-video-on-saturns-spinning-rings-375558
    # https://solarsystem.nasa.gov/planets/saturn/in-depth/#:~:text=Saturn's%20ring%20system%20extends%20up,meters)%20in%20the%20main%20rings.
    saturn_ring = PlanetRing(160000,
                    136780,
                    saturn,
                    1,
                    1.54 * 10**19,
                    PLANET_SCALE,
                    color=vector(.43, .4, .3451)) # RGB values as percentage R, G, and B
    uranus = Planet(51118,
                    2877000000,
                    -17.2,
                    84.014 * 365.25,
                    'new_textures/uranus.jpg',
                    86.8 * 10**24,
                    0.8,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)
    neptune = Planet(49528,
                    4503000000,
                    16.1,
                    167.78 * 365.25,
                    'new_textures/neptune.jpg',
                    102  * 10**24,
                    1.8,
                    sun,
                    PLANET_SCALE,
                    DISTANCE_SCALE,
                    time_scale,
                    REFRESH_RATE)

    solar_system = {'sun': sun,
                    'mercury': mercury,
                    'venus': venus,
                    'earth': earth,
                    'Lagrange 2': lagrange,
                    'moon': moon,
                    'satellite' : satellite,
                    'mars': mars,
                    'jupiter': jupiter,
                    'saturn': saturn,
                    'saturn_ring': saturn_ring,
                    'uranus': uranus,
                    'neptune': neptune,
                    'asteroid': asteroid
                    } #lagrange' : lagrange"""

    # Show scene now that assets are loaded
    #scene.waitfor('textures')
    #scene.visible = True

    button(text='<b>START</b>', pos=scene.title_anchor, bind=start_flag_button)
    scene.caption = ''
    menu(choices=['1s = 1h', '1s = 24h', '1s = 30days', '1s = 90days', '1s = 180days'], bind=time_scale_menu, pos=scene.title_anchor)
    menu(choices=list(solar_system.keys()), bind=camera_menu, pos=scene.title_anchor)
    button(text='trail', pos=scene.title_anchor, bind=trail_flag_button)

    for obj in list(solar_system.values()):
        if type(obj) == Star:
            obj.light_on()

    # MAIN LOOP:
    while True:
        rate(REFRESH_RATE)
        for obj in list(solar_system.values()):
            if type(obj) != PlanetRing:
                obj.update(time_scale)
            if start_flag:
                if type(obj) != PlanetRing:
                    obj.rotate_axis()
                if type(obj) == Planet:
                    if trail_flag:
                        obj.trail(0)
                    else:
                        obj.clear_trail()
                    if obj.sum_ang >= 2 * pi: # If
                        obj.clear_trail()
                        obj.sum_ang = 0
                if type(obj) != Star: #if type(obj) != Star and type(obj) != Lagrange:"
                    obj.rotate_orbit()
