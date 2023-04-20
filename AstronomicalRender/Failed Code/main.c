/* main.cpp: Backend for asteroid tracking 	    */
/* Name: Thomas Jordan 				            */
/* Date Created: Wed Feb  8 11:20:26 PST 2023   */
/* Last Modified: Wed Feb  8 11:20:26 PST 2023  */

#include <stdio.h>
#include <math.h>

/* Constants */
#define M 1.989e30
#define m 5.972e24
#define r1 151.65e6
#define PI 3.14159265358979323846

double f(double x) {
    return M*x*x + (r1+x)*(r1+x) * (m-(M/(r1*r1*r1))*x*x*(r1+x));
}

double f_(double f(double), double x) {
    double h = 0.0000001;
    return(f(x+h) - f(x))/h;
}

double f__(double f(double), double x) {
    double h = 0.0000001;
    return(f_(f,x+h) - f_(f,x))/h;
}

double nr(double f(double), double x0, double e) {
    double x1 = 0;
    int N = 1000, n = 1;
    printf("x0 = %lf\n", x0);

    while(n<N && fabs(f(x0)) > e) {
        double h = -f(x0)/f_(f,x0);
        x1 = x0+h;
        printf("%d %lf\n", n, x1);
        x0 = x1;
        n = n+1;
    }

    if (f(x0)<e) {
        return x0;
    } else {
        return NAN;
    }
}

int main(void) {
    double t;
    printf("At what time t do you want to find the coordinates of the satellite: ");
    scanf("%lf", &t);

    double length = (nr(f, 100) * 0.621371);
    printf("Newton-Raphson: \n");
    printf("root = %lf\n", length);

    double C = pow(7.06e6, 6);
    double T = C / ((365/2)*24);

    double height = r1*sin(2*PI*T);
    double width = r1*cos(2*PI*T);

    printf("x: %lf y: %lf z: %lf\n", width, length, height);

    return 0;
}
