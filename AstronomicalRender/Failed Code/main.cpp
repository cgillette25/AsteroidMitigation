//
//  main.cpp
//  Asteroid
//
//  Created by Chaz Gillette on 3/1/23.
//
 /*
  
  Below is a code outline for how to code the Satellite location. I have layed out functions to hopefully make the math clear but obciously, code it however you'd like. If you have questions,please shoot me a text.  Thank you.
  
  
  t = time (get user input and store)
  Rl_2 = the radius distance to the James Webb Space telescope (hardcode)
  
  Function 1: P
  Pl_2 is a vector with two values <x,y>
  x = Rl_2 * cos(t);
  y = Rl_2 * sin(t);
  
  Function 2: P'
  
  x = -Rl_2 * sin(t);
  y = Rl_2 cos(t);
  
  Function 3: T'
  
  x = -Rl_2 * cos(t);
  y =  -Rl_2 * sin(t);
  
  
  
  Function 4: Mag
  Mag is the magnitude of a 2D vector. It will take in the two values i, j (like x, y) as parameters and return the magnitdude
  Mag = sqrt(i^2 + j ^2);
  
  Function 5: T
  T is the Tangential vector
  
  T = P'/Mag(P');
  
  Will return two value vector using other functions.
  
  
  
  Function 6: N
  N is the normal vector
  
  N = T'/Mag(T')
  
  
  Function 7: B
  B is the binormal vector
  
  B = T x N
  
  B is the cross product of T and N.
  
  Function 8: Dot Product
  
  Returns dot product of two input parameters (I'm still thinking about the best approach to code this given the equation, you can hold off on this unless you're feeling spunky and want to figure it out lol)
  
  Function 9: Returning 3D Vector Location
  
  3D vector will have values <x,y,z>
  
  x = P
  y = Dot Product(Rl_2*cos(2t), T)
  z = Dot Product(Rl_2*sin2T, B)

  
  */