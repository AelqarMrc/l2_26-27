#include <stdlib.h>
#include <stdio.h>
#include "somme.h"

unsigned int somme1(unsigned int n){
    if (n == 0)
        return 0;
    else
        return n + somme1(n-1);
}

unsigned int somme2(unsigned int n){
    return somme2R(n,0);
}

unsigned int somme2R(unsigned int n, unsigned int acc){
    if (n == 0)
        return acc;
    else
        return somme2R(n-1, acc + n);
}