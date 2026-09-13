#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "somme.h"

int main(void){

    unsigned int n;
    printf("Entrez la valeur des n premiers entiers positifs : ");
    scanf("%d", &n);

    printf("somme des %d premiers entiers positifs est : %d\n", n, somme2(n));

    return EXIT_SUCCESS;
}