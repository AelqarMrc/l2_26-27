#include <stdlib.h>
#include <stdio.h>
#include "point.h"
#include "tab_point.h"

indices distMinMax(Tab_point t, int taille){
    indices ind;
    ind.i = t;
    ind.j = t;

    int i = 0;

    while (i < taille)
    {
        if (distanceO(t[i])<distanceO(t[i+1]))
            ind.i = i+1;
        else if (distanceO(t[i])>distanceO(t[i+1]))
            ind.j = i+1;
    }

    return ind;
}

void triDist(Tab_point *t, int taille){
    
}