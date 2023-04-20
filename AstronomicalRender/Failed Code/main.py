import math as math
import math
mod = math.fabs

t = input("At what time t do you want to find the coordinates of the satellite: ")

M = 1.989*10**30
m = 5.972*10**24
r1 = 151.65*10**6

def f(x):
    return M*x**2 + (r1+x)**2 * (m-(M/(r1**3))*x**2*(r1+x))

def f_(f,x):
    h = 0.0000001
    return(f(x+h) - f(x))/h

def f__(f,x):
    h = 0.0000001
    return(f_(f,x+h)-f_(f,x))/h

def nr(f, x0, e=0.00001):
    x1 = None
    N = 1000
    n = 1
    print("x0 = ", x0)

    while(n<N and mod(f(x0)) > e):
        h = -f(x0)/f_(f,x0)
        x1 = x0+h
        print(n, x1)
        x0 = x1
        n = n+1
    return x0 if f(x0)<e else "Max Iteration Exceeded"


length = (nr(f, 100) * 0.621371)
print("Newton-Raphson: \n")
print("root = ", length, "\n")


C = 7.06*10**6
T = C / ((365/2)*24)

height = r1*math.sin(2*3.14*T)
width = r1*math.cos(2*3.14*T)

print("x: ", width, "y: ", length, "z: ", height)



