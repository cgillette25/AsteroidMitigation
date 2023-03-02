# Meeting with Dr. John
* Function (t) to calculate the satellites position in orbit around the Lagrange point
* Function (t) to calculate the position of earth in its orbit
* Function to construct a vector that points at an asteroid
	* THERE IS ALREADY CODE FOR THIS
	* Read about Kepler’s Laws
	* Read about planetary dynamics
	* http://alpheratz.net/dynamics/twobody/KeplerIterations_summary.pdf
	* [Kepler’s laws of planetary motion - Wikipedia](https://en.wikipedia.org/wiki/Kepler%27s_laws_of_planetary_motion)
* Parabola and Conic Cylinder 
	* Extrinsic Conics Equations
	* Eccentricity is the ratio of the line between center and parabola and the ratio between the the distance from the parabola to the line it was constructed from
		* https://openstax.org/books/calculus-volume-3/pages/1-5-conic-sections
Force_sun + Force_earth = mass_asteroid * acceleration_asteroid
(GM_sun * m_asteroid / |r_sun|^2)  * r_sun/|r_sun| + GM_earth*m_asteroid / |r_earth|^2 * r_e = mass_asteroid * acceleration_asteroid
Thus
GM_s*r_a / |r_a|^3 + GM_e(r_a)-(r_e) / \r_a-r_e|^3 = m_asteroid * acceleration_asteroid = m_asteroid * r’’_a
If we know (initial conditions)
r_a of asteroid at t=0 position
r’_a of asteroid at t = 0 velocity
 Let’s call GM_s and GM_e as K_s and K_e respectively
K_s * r_a / |r_a|^3 + K_e * r_a - r_e / ||r_a - r_e|| ^3 = m r’’_a

F(t) earth takes around the sun -> known
Mass of asteroid (needs to be estimated) 
r_a = ks<x_a, y_a, z_a> / <x_a + y_a + z_a>^3/2 + ke <x_a - x_e, y_x - y_e, z_a - z_e> / (x_a - x_e)^2 + (y_x - y_e)^2 + (z_a - z_e)^2)^3/2 = m<x_a’’, y_a’’, z_a’’>
How do we simulate this from t=0 to t=n
Solution of differential equations
Entire equation is dependent on position (left side of the equation)
Continous time broken down to discrete 

Newtom Raphsum: https://personal.math.ubc.ca/~anstee/math104/104newtonmethod.pdf
Numerical Simulation of ODEs: https://services.math.duke.edu/~holee/math361-2020/lectures/Lec7-ODEs.pdf

Satellite can work independently from earth

Other Notes:
* [Example: Plotting Lagrange Points — Orbital Mechanics & Astrodynamics](https://orbital-mechanics.space/the-n-body-problem/Lagrange-points-example.html)