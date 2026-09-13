#include <stdlib.h> 
#include <stdio.h> 
#include <time.h>

unsigned int puiss1R(double x, unsigned int n, int acc);
unsigned int puiss1(double x, unsigned int n){
    return puiss1R(x,n,0);
}

unsigned int puiss1R(double x, unsigned int n, int acc){
    if (n==0)
        return 1;
    else if (n%2 == 1)
        return x*puiss1R(x, n-1, acc*n);
    else 
        return puiss1R(x*x, n/2, acc*n);
}


int main(void){

    clock_t debut,fin;

    debut = clock();
        printf("%d\n",puiss1(2,2));
    fin = clock();

    double temps = (fin - debut +0.0)/CLOCKS_PER_SEC;
    
    printf("%lf\n", temps);
    

    return EXIT_SUCCESS;
}
