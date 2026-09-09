#include <stdlib.h>
#include <stdio.h>
#include "temps.h"

int main (void){

    _Bool b = 2;
    temps t1 = creer(2,10,30);
    printf("Valeur de verif t1 : %d\n", correct(t1));
    afficher(t1);
    printf("\n");

    temps t2 = creer2();
    printf("Valeur de verif t2 : %d\n", correct(t2));
    afficher(t2);
    printf("\n");

    temps t3;
    saisir(&t3);
    printf("Valeur de verif t3 : %d\n", correct(t3));
    afficher(t3);
    printf("\n");

    t1 = normaliser(t1);
    t2 = normaliser(t2);
    t3 = normaliser(t3);

    afficher(t1);
    afficher(t2);
    afficher(t3);

    return EXIT_SUCCESS;
}