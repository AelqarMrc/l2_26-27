#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include "temps.h"

temps creer(int h, int m, double s){
    temps t;
    t.h = h; 
    t.m = m; 
    t.s = s;
    
    return t;
}

_Bool correct(temps t){
    if (t.h < 0 || t.m < 0 ||t.s < 0 || t.h >= 24 || t.m >= 60 ||t.s >= 60 )
        return false;
    else
        return true;
}

void afficher(temps t){
    printf("il est %dh %dm %.lfs\n",t.h,t.m,t.s);
}

temps normaliser(temps t){
    while ((t.m >= 60) || (t.s >= 60 || (t.h >= 24)))
    {
         if (t.s >= 60)
        {
            t.m += 1;
            t.s -= 60;
        }
        else if (t.m >= 60)
        {
            t.h += 1;
            t.m -= 60;
        }
        else if (t.h >= 24)
        {
            t.h = t.h-24;
        }
    }
    return t;
}

temps creer2(void){
    temps t;

    printf("Enter a value for hour : ");
    scanf("%d",&t.h);
    printf("Enter a value for minute : ");
    scanf("%d",&t.m);
    printf("Enter a value for seconde : ");
    scanf("%lf",&t.s);

    return t;
}

void saisir(temps* pt){
    printf("Enter a value for hour : ");
    scanf("%d",&(pt->h));
    printf("Enter a value for minute : ");
    scanf("%d",&(pt->m));
    printf("Enter a value for seconde : ");
    scanf("%lf",&(pt->s));
}