#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include "point.h"

void remplir(point *pp){
    srand(time(NULL));

    pp->x = (-3.1) + (5+3.1) * rand() / RAND_MAX;
    pp->y = (-3.1) + (5+3.1) * rand() / RAND_MAX;
}

void affichage(point p){
    printf("Point( %.2lf ; %.2lf )\n", p.x, p.y);
}

double distance0(point p){
    double res = sqrt((p.x*p.x)+(p.y*p.y));

    return res;
}